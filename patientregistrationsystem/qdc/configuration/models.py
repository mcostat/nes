from typing import Any

from custom_user.models import Institution
from django.db import models
from solo.models import SingletonModel


def get_institution_logo_dir(instance: Any, filename: str) -> str:
    return f"institution_logo/{instance.id}/{filename}"


class LocalInstitution(SingletonModel):
    code = models.CharField(max_length=150, null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

    url = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to=get_institution_logo_dir, null=True, blank=True)

    def __str__(self) -> str:
        return "Local Institution"

    class Meta:
        verbose_name = "Local Institution"


class Contact(SingletonModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Contact"


class RightsSupport(models.Model):
    class Meta:
        managed = False

        permissions = [
            ("upgrade_rights", "Can upgrade NES version"),
        ]


class UsefulLink(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self) -> str:
        return f"{self.name}"
