from typing import Any

from django.forms import (
    BooleanField,
    CharField,
    CheckboxInput,
    CheckboxSelectMultiple,
    ChoiceField,
    Form,
    IntegerField,
    ModelForm,
    MultipleChoiceField,
    NumberInput,
    Select,
    SelectMultiple,
    TextInput,
)
from django.utils.translation import gettext_lazy as _
from patient.models import Diagnosis, Patient

HEADINGS_CHOICES = (
    ("code", _("Question code")),
    ("full", _("Full question text")),
    ("abbreviated", _("Abbreviated question text")),
)

RESPONSES_CHOICES = (
    ("short", _("Answer codes")),
    ("long", _("Full answers")),
)

FORMATS_CHOICES = (
    ("csv", _("Comma separated values")),
    ("tsv", _("Tab separated values")),
)


class ExportForm(Form):
    title = CharField(
        required=False,
        widget=TextInput(attrs={"class": "form-control", "disabled": ""}),
    )
    per_participant = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_questionnaire = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_eeg_raw_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_eeg_nwb_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_emg_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_tms_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_additional_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_goalkeeper_game_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_stimulus_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_generic_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )
    per_media_data = BooleanField(
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        initial=True,
        required=False,
    )

    questionnaire_entrance_selected: list = []

    headings = ChoiceField(
        widget=Select(attrs={"class": "form-select"}),
        choices=HEADINGS_CHOICES,
        required=False,
    )
    responses = MultipleChoiceField(
        widget=CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input",
                "data-error": _("Response must be selected"),
            },
        ),
        choices=RESPONSES_CHOICES,
        required=False,
    )
    filesformat = ChoiceField(
        widget=Select(attrs={"class": "form-select"}),
        choices=FORMATS_CHOICES,
        required=False,
    )


class ParticipantsSelectionForm(ModelForm):
    class Meta:
        model = Patient

        fields = [
            "gender",
            "marital_status",
            "country",
            "city",
            "state",
        ]

        widgets = {
            "gender": SelectMultiple(attrs={"class": "form-select", "disabled": ""}),
            "marital_status": SelectMultiple(attrs={"class": "form-select", "disabled": ""}),
            "country": SelectMultiple(attrs={"class": "form-select", "disabled": ""}),
            "state": SelectMultiple(attrs={"class": "form-select", "disabled": ""}),
            "city": SelectMultiple(attrs={"class": "form-select", "disabled": ""}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["gender"].empty_label = None
        self.fields["marital_status"].empty_label = None
        self.fields["country"].empty_label = None
        self.fields["state"].empty_label = None
        self.fields["city"].empty_label = None

        self.fields["gender"].required = True
        self.fields["marital_status"].required = True
        self.fields["country"].required = True
        self.fields["state"].required = True
        self.fields["city"].required = True

        if not self.data.get("gender"):
            self.fields["gender"].required = False
        if not self.data.get("marital_status"):
            self.fields["marital_status"].required = False
        if not self.data.get("country"):
            self.fields["country"].required = False
        if not self.data.get("state"):
            self.fields["state"].required = False
        if not self.data.get("city"):
            self.fields["city"].required = False


class AgeIntervalForm(Form):
    min_age = IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "required": "",
                "min": "0",
                "max": "999",
                "data-error": _("Min age must be filled."),
                "disabled": "",
            },
        ),
    )
    max_age = IntegerField(
        min_value=0,
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "required": "",
                "min": "0",
                "max": "999",
                "data-error": _("Max age must be filled."),
                "disabled": "",
            },
        ),
    )

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        assert cleaned_data is not None
        min_age = cleaned_data.get("min_age")
        max_age = cleaned_data.get("max_age")

        if max_age and min_age and max_age < min_age:
            msg = "Idade mínima deve ser menor que idade máxima."
            self._errors["min_age"] = self.error_class([msg])
            self._errors["max_age"] = self.error_class([msg])

            del cleaned_data["min_age"]
            del cleaned_data["max_age"]

        return cleaned_data


class DiagnosisSelectionForm(ModelForm):
    class Meta:
        model = Diagnosis

        fields = ["description"]

        widgets = {
            "description": SelectMultiple(attrs={"class": "form-select", "required": "", "disabled": ""}),
        }
