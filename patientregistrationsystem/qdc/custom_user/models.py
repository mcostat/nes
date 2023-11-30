from django.contrib.auth import get_user_model
from django.core.cache import caches
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta
from patient.models import COUNTRIES

LOGIN = (
    (False, _("No")),
    (True, _("Yes, a username and password must be configured")),
)


class Institution(models.Model):  # type: ignore [django-manager-missing]
    name = models.CharField(max_length=150)
    acronym = models.CharField(max_length=30, unique=True)
    country = models.CharField(max_length=30, choices=COUNTRIES)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children+",
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta(TypedModelMeta):
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(fields=["name", "acronym", "country"], name="unique_institution"),
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="user_profile")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)
    login_enabled = models.BooleanField(default=False, choices=LOGIN)
    force_password_change = models.BooleanField(default=True)
    citation_name = models.CharField(max_length=150, blank=True, default="")

    @staticmethod
    def cached_force_password_change(_user) -> bool:
        key = f"pw_change_{_user.username}"
        cache = caches["redis"]
        pw_change = cache.get(key)

        if isinstance(pw_change, bool):
            return pw_change

        profile = UserProfile.objects.filter(user=_user).first()

        if isinstance(profile, UserProfile):
            cache.set(key, profile.force_password_change, 30 * 60)

            return profile.force_password_change

        return False


@receiver((post_delete, post_save), sender=UserProfile)
def invalidate_force_password_change_cache(sender, instance, **kwargs) -> None:
    """
    Invalidate the book cached data when a book is changed or deleted
    """
    key = f"pw_change_{instance.user.username}"
    caches["redis"].delete(key)


def create_user_profile_signal(sender, instance, created, **kwargs) -> None:
    if created:
        UserProfile.objects.create(user=instance)


def password_change_signal(sender, instance, **kwargs) -> None:
    try:
        if get_user_model().objects.all().count() == 0:
            return

        user = get_user_model().objects.get(username=instance.username)

        if user.is_superuser:
            return

        if user.password != instance.password:
            profile, _created = UserProfile.objects.get_or_create(user=user)
            profile.force_password_change = False
            profile.save()
    except get_user_model().DoesNotExist:
        pass


signals.pre_save.connect(password_change_signal, sender=get_user_model(), dispatch_uid="accounts.models")

signals.post_save.connect(create_user_profile_signal, sender=get_user_model(), dispatch_uid="accounts.models")
