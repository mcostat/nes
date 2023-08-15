# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
import patient.models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AlcoholFrequency",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_pt_BR", models.CharField(null=True, max_length=100)),
                ("name_en", models.CharField(null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="AlcoholPeriod",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="AmountCigarettes",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ClassificationOfDiseases",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=300)),
                ("description_pt_BR", models.CharField(null=True, max_length=300)),
                ("description_en", models.CharField(null=True, max_length=300)),
                ("abbreviated_description", models.CharField(max_length=190)),
                (
                    "abbreviated_description_pt_BR",
                    models.CharField(null=True, max_length=190),
                ),
                (
                    "abbreviated_description_en",
                    models.CharField(null=True, max_length=190),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.ClassificationOfDiseases",
                        related_name="children",
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ComplementaryExam",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("description", models.CharField(max_length=500)),
                ("doctor", models.CharField(blank=True, null=True, max_length=50)),
                (
                    "doctor_register",
                    models.CharField(blank=True, null=True, max_length=10),
                ),
                ("exam_site", models.CharField(blank=True, null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Diagnosis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(null=True)),
                ("description", models.CharField(null=True, max_length=300)),
                (
                    "classification_of_diseases",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to="patient.ClassificationOfDiseases"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExamFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.FileField(upload_to=patient.models.get_user_dir)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to="patient.ComplementaryExam"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FleshTone",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalPatient",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        verbose_name="ID", blank=True, db_index=True, auto_created=True
                    ),
                ),
                ("code", models.CharField(db_index=True, max_length=10)),
                ("name", models.CharField(blank=True, null=True, max_length=50)),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        db_index=True,
                        validators=[patient.models.validate_cpf],
                        null=True,
                    ),
                ),
                ("origin", models.CharField(blank=True, null=True, max_length=50)),
                (
                    "medical_record",
                    models.CharField(blank=True, null=True, max_length=25),
                ),
                (
                    "date_birth",
                    models.DateField(validators=[patient.models.validate_date_birth]),
                ),
                ("rg", models.CharField(blank=True, null=True, max_length=15)),
                ("country", models.CharField(blank=True, null=True, max_length=30)),
                ("zipcode", models.CharField(blank=True, null=True, max_length=12)),
                ("street", models.CharField(blank=True, null=True, max_length=50)),
                ("address_number", models.IntegerField(blank=True, null=True)),
                (
                    "address_complement",
                    models.CharField(blank=True, null=True, max_length=50),
                ),
                ("district", models.CharField(blank=True, null=True, max_length=50)),
                ("city", models.CharField(blank=True, null=True, max_length=30)),
                ("state", models.CharField(blank=True, null=True, max_length=30)),
                ("email", models.EmailField(blank=True, null=True, max_length=254)),
                ("removed", models.BooleanField(default=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        max_length=1,
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        to="patient.Gender",
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical patient",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="HistoricalSocialDemographicData",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        verbose_name="ID", blank=True, db_index=True, auto_created=True
                    ),
                ),
                ("natural_of", models.CharField(blank=True, null=True, max_length=50)),
                ("citizenship", models.CharField(blank=True, null=True, max_length=50)),
                ("profession", models.CharField(blank=True, null=True, max_length=50)),
                ("occupation", models.CharField(blank=True, null=True, max_length=50)),
                ("benefit_government", models.BooleanField(null=True)),
                ("tv", models.IntegerField(blank=True, null=True)),
                ("dvd", models.IntegerField(blank=True, null=True)),
                ("radio", models.IntegerField(blank=True, null=True)),
                ("bath", models.IntegerField(blank=True, null=True)),
                ("automobile", models.IntegerField(blank=True, null=True)),
                ("wash_machine", models.IntegerField(blank=True, null=True)),
                ("refrigerator", models.IntegerField(blank=True, null=True)),
                ("freezer", models.IntegerField(blank=True, null=True)),
                ("house_maid", models.IntegerField(blank=True, null=True)),
                (
                    "social_class",
                    models.CharField(blank=True, null=True, max_length=10),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        max_length=1,
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "flesh_tone",
                    models.ForeignKey(
                        to="patient.FleshTone",
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical social demographic data",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="HistoricalSocialHistoryData",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        verbose_name="ID", blank=True, db_index=True, auto_created=True
                    ),
                ),
                ("smoker", models.BooleanField(null=True)),
                ("ex_smoker", models.BooleanField(null=True)),
                ("alcoholic", models.BooleanField(null=True)),
                ("drugs", models.CharField(blank=True, null=True, max_length=25)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        max_length=1,
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                    ),
                ),
                (
                    "alcohol_frequency",
                    models.ForeignKey(
                        to="patient.AlcoholFrequency",
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "alcohol_period",
                    models.ForeignKey(
                        to="patient.AlcoholPeriod",
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "amount_cigarettes",
                    models.ForeignKey(
                        to="patient.AmountCigarettes",
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical social history data",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="HistoricalTelephone",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        verbose_name="ID", blank=True, db_index=True, auto_created=True
                    ),
                ),
                ("number", models.CharField(max_length=15)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        choices=[
                            ("MO", "Cell phone"),
                            ("HO", "Home phone"),
                            ("WO", "Business"),
                            ("MA", "Main"),
                            ("FW", "Business fax"),
                            ("FH", "Home fax"),
                            ("PA", "Pager"),
                            ("OT", "Other"),
                        ],
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=50)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        max_length=1,
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        db_constraint=False,
                        blank=True,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        related_name="+",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical telephone",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
        ),
        migrations.CreateModel(
            name="MaritalStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="MedicalRecordData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("record_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "permissions": (
                    ("view_medicalrecorddata", "Can view medical record"),
                    ("export_medicalrecorddata", "Can export medical record"),
                ),
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(blank=True, null=True, max_length=50)),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        unique=True,
                        validators=[patient.models.validate_cpf],
                        null=True,
                    ),
                ),
                ("origin", models.CharField(blank=True, null=True, max_length=50)),
                (
                    "medical_record",
                    models.CharField(blank=True, null=True, max_length=25),
                ),
                (
                    "date_birth",
                    models.DateField(validators=[patient.models.validate_date_birth]),
                ),
                ("rg", models.CharField(blank=True, null=True, max_length=15)),
                ("country", models.CharField(blank=True, null=True, max_length=30)),
                ("zipcode", models.CharField(blank=True, null=True, max_length=12)),
                ("street", models.CharField(blank=True, null=True, max_length=50)),
                ("address_number", models.IntegerField(blank=True, null=True)),
                (
                    "address_complement",
                    models.CharField(blank=True, null=True, max_length=50),
                ),
                ("district", models.CharField(blank=True, null=True, max_length=50)),
                ("city", models.CharField(blank=True, null=True, max_length=30)),
                ("state", models.CharField(blank=True, null=True, max_length=30)),
                ("email", models.EmailField(blank=True, null=True, max_length=254)),
                ("removed", models.BooleanField(default=False)),
                (
                    "changed_by",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(on_delete=models.CASCADE, to="patient.Gender"),
                ),
                (
                    "marital_status",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.MaritalStatus",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("view_patient", "Can view patient"),
                    ("export_patient", "Can export patient"),
                    ("sensitive_data_patient", "Can view sensitive patient data"),
                ),
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionnaireResponse",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token_id", models.IntegerField()),
                (
                    "date",
                    models.DateField(
                        default=datetime.date.today,
                        validators=[
                            patient.models.validate_date_questionnaire_response
                        ],
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(on_delete=models.CASCADE, to="patient.Patient"),
                ),
                (
                    "questionnaire_responsible",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "survey",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="survey.Survey"
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("view_questionnaireresponse", "Can view questionnaire response"),
                    (
                        "export_questionnaireresponse",
                        "Can export questionnaire response",
                    ),
                ),
            },
        ),
        migrations.CreateModel(
            name="Religion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Schooling",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_pt_BR", models.CharField(null=True, max_length=50)),
                ("name_en", models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="SocialDemographicData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("natural_of", models.CharField(blank=True, null=True, max_length=50)),
                ("citizenship", models.CharField(blank=True, null=True, max_length=50)),
                ("profession", models.CharField(blank=True, null=True, max_length=50)),
                ("occupation", models.CharField(blank=True, null=True, max_length=50)),
                ("benefit_government", models.BooleanField(null=True)),
                ("tv", models.IntegerField(blank=True, null=True)),
                ("dvd", models.IntegerField(blank=True, null=True)),
                ("radio", models.IntegerField(blank=True, null=True)),
                ("bath", models.IntegerField(blank=True, null=True)),
                ("automobile", models.IntegerField(blank=True, null=True)),
                ("wash_machine", models.IntegerField(blank=True, null=True)),
                ("refrigerator", models.IntegerField(blank=True, null=True)),
                ("freezer", models.IntegerField(blank=True, null=True)),
                ("house_maid", models.IntegerField(blank=True, null=True)),
                (
                    "social_class",
                    models.CharField(blank=True, null=True, max_length=10),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "flesh_tone",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.FleshTone",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(on_delete=models.CASCADE, to="patient.Patient"),
                ),
                (
                    "patient_schooling",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="Schooling of the patient",
                        to="patient.Schooling",
                        blank=True,
                        related_name="patient_schooling_set",
                        null=True,
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.Payment",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "religion",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.Religion",
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "schooling",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        verbose_name="Schooling of the householder",
                        to="patient.Schooling",
                        blank=True,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SocialHistoryData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("smoker", models.BooleanField(null=True)),
                ("ex_smoker", models.BooleanField(null=True)),
                ("alcoholic", models.BooleanField(null=True)),
                ("drugs", models.CharField(blank=True, null=True, max_length=25)),
                (
                    "alcohol_frequency",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.AlcoholFrequency",
                        default=0,
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "alcohol_period",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.AlcoholPeriod",
                        default=0,
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "amount_cigarettes",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="patient.AmountCigarettes",
                        default=0,
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(on_delete=models.CASCADE, to="patient.Patient"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Telephone",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        auto_created=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=15)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        choices=[
                            ("MO", "Cell phone"),
                            ("HO", "Home phone"),
                            ("WO", "Business"),
                            ("MA", "Main"),
                            ("FW", "Business fax"),
                            ("FH", "Home fax"),
                            ("PA", "Pager"),
                            ("OT", "Other"),
                        ],
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=50)),
                (
                    "changed_by",
                    models.ForeignKey(
                        on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(on_delete=models.CASCADE, to="patient.Patient"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="medicalrecorddata",
            name="patient",
            field=models.ForeignKey(on_delete=models.CASCADE, to="patient.Patient"),
        ),
        migrations.AddField(
            model_name="medicalrecorddata",
            name="record_responsible",
            field=models.ForeignKey(
                on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="historicaltelephone",
            name="patient",
            field=models.ForeignKey(
                to="patient.Patient",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialhistorydata",
            name="patient",
            field=models.ForeignKey(
                to="patient.Patient",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialdemographicdata",
            name="patient",
            field=models.ForeignKey(
                to="patient.Patient",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialdemographicdata",
            name="patient_schooling",
            field=models.ForeignKey(
                to="patient.Schooling",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialdemographicdata",
            name="payment",
            field=models.ForeignKey(
                to="patient.Payment",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialdemographicdata",
            name="religion",
            field=models.ForeignKey(
                to="patient.Religion",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalsocialdemographicdata",
            name="schooling",
            field=models.ForeignKey(
                to="patient.Schooling",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="historicalpatient",
            name="marital_status",
            field=models.ForeignKey(
                to="patient.MaritalStatus",
                db_constraint=False,
                blank=True,
                related_name="+",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
            ),
        ),
        migrations.AddField(
            model_name="diagnosis",
            name="medical_record_data",
            field=models.ForeignKey(
                on_delete=models.CASCADE, to="patient.MedicalRecordData"
            ),
        ),
        migrations.AddField(
            model_name="complementaryexam",
            name="diagnosis",
            field=models.ForeignKey(on_delete=models.CASCADE, to="patient.Diagnosis"),
        ),
        migrations.AlterUniqueTogether(
            name="diagnosis",
            unique_together=set(
                [("medical_record_data", "classification_of_diseases")]
            ),
        ),
    ]
