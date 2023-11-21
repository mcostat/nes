from django.contrib.auth.forms import PasswordChangeForm
from django.forms import PasswordInput, ValidationError
from django.utils.translation import gettext_lazy as _
from qdc.utils import PASSWORD_MIN_LEN, PASSWORD_REGEX


class PasswordChangeFormCustomized(PasswordChangeForm):
    _password_regex: str = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget = PasswordInput(
            attrs={
                "class": "form-control",
                "autofocus": "true",
                "required": "",
                "placeholder": _("Current password"),
                "autocomplete": "current-password",
            }
        )

        self.fields["new_password1"].widget = PasswordInput(
            attrs={
                "class": "form-control",
                "required": "",
                "minlength": "8",
                "maxlength": "128",
                "data-error": _(
                    f"Password must contain at least{PASSWORD_MIN_LEN} characters, "
                    "including at least one uppercase letter, digit or special character."
                ),
                "title": _(
                    f"Password must contain at least {PASSWORD_MIN_LEN} characters, "
                    "including at least one uppercase letter, digit or special character."
                ),
                "pattern": PASSWORD_REGEX,
                # "pattern": self._password_regex,
                "placeholder": _("New password"),
                "autocomplete": "new-password",
            }
        )

        self.fields["new_password2"].widget = PasswordInput(
            attrs={
                "class": "form-control",
                "required": "",
                "minlength": "8",
                "data-match": "#id_new_password1",
                "placeholder": _("Confirm new password"),
                "data-error": _("Passwords don't match"),
                "title": _("Passwords don't match"),
                "autocomplete": "new-password",
            }
        )

    def clean_new_password1(self) -> str:
        password1: str = self.cleaned_data["new_password1"]

        # At least MIN_LENGTH long
        if len(password1) < PASSWORD_MIN_LEN:
            raise ValidationError(_(f"The new password must be at least {PASSWORD_MIN_LEN} characters long."))

        #  at least one uppercase letter, digit or special character
        ok = False
        for character in password1:
            if character.isupper() or character.isdigit() or character in r"!@#$%&()*+,-./:;<=>?[\]_{|}~'":
                ok = True
                break
        if not ok:
            raise ValidationError(
                _(
                    f"Password must contain at least {PASSWORD_MIN_LEN} characters,"
                    "including at least one uppercase letter, digit or special character."
                ),
            )

        return password1
