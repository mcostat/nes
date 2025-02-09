from django import forms
from django.core.validators import EMPTY_VALUES
from django.forms import CheckboxInput, ModelForm, RadioSelect, Select, TextInput, TypedChoiceField
from django.forms.widgets import Textarea
from django.utils.translation import gettext as _
from patient.models import (
    ComplementaryExam,
    ExamFile,
    Patient,
    QuestionnaireResponse,
    SocialDemographicData,
    SocialHistoryData,
    Telephone,
)
from qdc.utils import DATE_REGEX, FULLNAME_REGEX, PHONE_REGEX

NULLBOOLEAN_CHOICE = ((True, _("Yes")), (False, _("No")), (None, _("Unknown")))
RATINGS_CHOICE = ((0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, _("4 or +")))


class PatientForm(ModelForm):
    anonymous = forms.BooleanField(
        required=False,
        initial=False,
        label=_("Anonymous participant?"),
        widget=CheckboxInput(
            attrs={
                "class": "form-check-input",
            },
        ),
    )

    def __init__(self, data=None, *args, **kwargs) -> None:
        super().__init__(data, *args, **kwargs)
        self.fields["zipcode"].widget.attrs["onBlur"] = "pesquisacep(this.value);"
        self.fields["country"].initial = "BR"

    class Meta:
        model = Patient

        fields = [
            "anonymous",
            "name",
            "cpf",
            "origin",
            "medical_record",
            "date_birth",
            "gender",
            "rg",
            "marital_status",
            "country",
            "zipcode",
            "street",
            "address_number",
            "address_complement",
            "district",
            "city",
            "state",
            "email",
        ]

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    # "autofocus": "",
                    "required": "",
                    "data-error": _("Name must be included"),
                    "minlength": "2",
                    "maxlength": "50",
                    "pattern": FULLNAME_REGEX,
                    "oninput": "this.value = this.value.toUpperCase()",
                },
            ),
            "cpf": TextInput(attrs={"class": "form-control", "placeholder": "xxx.xxx.xxx-xx"}),
            "origin": TextInput(attrs={"class": "form-control"}),
            "medical_record": TextInput(attrs={"class": "form-control"}),
            "date_birth": TextInput(
                attrs={
                    "type": "date",
                    "pattern": DATE_REGEX,
                    "class": "form-control",
                    "required": "",
                    "placeholder": _("mm/dd/yyyy"),
                    "data-error": _("Date of birth must be completed"),
                },
            ),
            "gender": Select(
                attrs={
                    "class": "form-select",
                    "required": "",
                    "data-error": _("Gender must be filled"),
                },
            ),
            "rg": TextInput(
                attrs={
                    "class": "form-control",
                    "maxlength": "15",
                },
            ),
            "marital_status": Select(attrs={"class": "form-select"}),
            "country": Select(attrs={"class": "form-select"}),
            "zipcode": TextInput(
                attrs={
                    "type": "tel",
                    "class": "form-control",
                    "pattern": r"\d{5}-?\d{3}",
                },
            ),
            "street": TextInput(attrs={"class": "form-control"}),
            "address_number": TextInput(attrs={"class": "form-control"}),
            "address_complement": TextInput(attrs={"class": "form-control"}),
            "district": TextInput(attrs={"class": "form-control"}),
            "city": TextInput(attrs={"class": "form-control"}),
            "state": TextInput(attrs={"class": "form-control"}),
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "type": "email",
                    "data-error": _("Incorrect e-mail"),
                },
            ),
        }

    # Make the name required if anonymous field is not checked
    def clean(self):
        anonymous = self.cleaned_data.get("anonymous", False)
        if not anonymous:
            # validate the name
            name = self.cleaned_data.get("name", None)
            if name in EMPTY_VALUES:
                self._errors["name"] = self.error_class([_("Name must be included")])  # type: ignore
        return self.cleaned_data


class TelephoneForm(ModelForm):
    class Meta:
        model = Telephone

        fields = ["number", "type", "note"]

        widgets = {
            "number": TextInput(
                attrs={
                    "type": "tel",
                    "class": "form-control telephone_number",
                    # "pattern": r"^[- ()0-9]+",
                    "pattern": PHONE_REGEX,
                },
            ),
            "type": Select(attrs={"class": "form-select"}),
            "note": TextInput(attrs={"class": "form-control"}),
        }


class SocialDemographicDataForm(ModelForm):
    benefit_government = TypedChoiceField(
        required=False,
        empty_value=None,
        choices=((True, _("Yes")), (False, _("No"))),
        widget=RadioSelect(
            attrs={
                "class": "form-check-input",
            },
        ),
    )

    class Meta:
        model = SocialDemographicData
        fields = [
            "natural_of",
            "citizenship",
            "profession",
            "occupation",
            "tv",
            "dvd",
            "radio",
            "bath",
            "automobile",
            "wash_machine",
            "refrigerator",
            "freezer",
            "house_maid",
            "religion",
            "payment",
            "flesh_tone",
            "patient_schooling",
            "schooling",
            "benefit_government",
            "social_class",
        ]
        widgets = {
            "natural_of": TextInput(attrs={"class": "form-control"}),
            "citizenship": Select(attrs={"class": "form-select"}),
            "patient_schooling": Select(attrs={"class": "form-select"}),
            "schooling": Select(attrs={"class": "form-select"}),
            "flesh_tone": Select(attrs={"class": "form-select"}),
            "religion": Select(attrs={"class": "form-select"}),
            "profession": TextInput(attrs={"class": "form-control", "placeholder": _("Type in profession")}),
            "occupation": TextInput(attrs={"class": "form-control", "placeholder": _("Inform occupation")}),
            "payment": Select(attrs={"class": "form-select"}),
            "tv": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "dvd": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "radio": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "bath": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "automobile": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "house_maid": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "wash_machine": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "refrigerator": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "freezer": RadioSelect(
                choices=RATINGS_CHOICE,
                attrs={
                    "class": "form-check-input",
                },
            ),
            "social_class": TextInput(attrs={"class": "form-control", "readonly": ""}),
        }


class SocialHistoryDataForm(ModelForm):
    smoker = TypedChoiceField(
        required=False,
        empty_value=None,
        choices=NULLBOOLEAN_CHOICE,
        widget=RadioSelect(
            attrs={
                "class": "form-check-input",
                "id": "id_smoker",
            },
        ),
    )
    ex_smoker = TypedChoiceField(
        required=False,
        empty_value=None,
        choices=NULLBOOLEAN_CHOICE,
        widget=Select(
            attrs={
                "class": "form-select",
            },
        ),
    )
    alcoholic = TypedChoiceField(
        required=False,
        empty_value=None,
        choices=NULLBOOLEAN_CHOICE,
        widget=RadioSelect(
            attrs={
                "class": "form-check-input",
                "id": "id_alcoholic",
            },
        ),
    )

    class Meta:
        model = SocialHistoryData
        fields = [
            "smoker",
            "amount_cigarettes",
            "ex_smoker",
            "alcoholic",
            "alcohol_frequency",
            "alcohol_period",
            "drugs",
            "medical_drugs_history",
        ]

        widgets = {
            "amount_cigarettes": Select(attrs={"class": "form-select"}),
            "alcohol_frequency": Select(attrs={"class": "form-select"}),
            "alcohol_period": Select(attrs={"class": "form-select"}),
            "drugs": RadioSelect(
                attrs={"class": "form-check-input"},
                choices=(
                    ("ja_fez", _("Have already used")),
                    ("faz", _("It is using")),
                    ("nunca_fez", _("Have never used")),
                    (None, _("Unknown")),
                ),
            ),
            "medical_drugs_history": Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "4",
                },
            ),
        }


class ComplementaryExamForm(ModelForm):
    class Meta:
        model = ComplementaryExam
        fields = ["date", "description", "doctor", "doctor_register", "exam_site"]

        widgets = {
            "date": TextInput(
                attrs={
                    "type": "date",
                    "pattern": DATE_REGEX,
                    "class": "form-control",
                    "placeholder": _("mm/dd/yyyy"),
                    "required": "",
                    "data-error": _("Date must be completed"),
                },
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Description"),
                    "style": "resize: vertical;",
                    "rows": "4",
                    "required": "",
                    "data-error": _("Description must be filled in"),
                },
            ),
            "doctor": TextInput(attrs={"class": "form-control", "placeholder": _("Doctor")}),
            "doctor_register": TextInput(attrs={"class": "form-control", "placeholder": _("CRM")}),
            "exam_site": TextInput(attrs={"class": "form-control", "placeholder": _("Place of execution")}),
        }


class ExamFileForm(ModelForm):
    class Meta:
        model = ExamFile
        fields = ["content"]


class QuestionnaireResponseForm(ModelForm):
    class Meta:
        model = QuestionnaireResponse
        fields = ["date"]

        widgets = {
            "date": TextInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "pattern": DATE_REGEX,
                    "placeholder": _("mm/dd/yyyy"),
                    "required": "",
                    "data-error": _("Fill date must be filled."),
                },
            ),
        }
