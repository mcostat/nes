# Generated by Django 4.2.5 on 2023-09-08 19:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import experiment.models
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiment", "0003_alter_componentconfiguration_random_position"),
    ]

    operations = [
        migrations.CreateModel(
            name="MediaCollectionData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.date.today,
                        validators=[
                            experiment.models.validate_date_questionnaire_response
                        ],
                    ),
                ),
                ("time", models.TimeField(blank=True, null=True)),
                ("description", models.TextField()),
                (
                    "file_format_description",
                    models.TextField(blank=True, default="", null=True),
                ),
                (
                    "data_configuration_tree",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiment.dataconfigurationtree",
                    ),
                ),
                (
                    "file_format",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiment.fileformat",
                    ),
                ),
                (
                    "subject_of_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiment.subjectofgroup",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MediaCollectionFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to=experiment.models.get_data_file_dir),
                ),
                (
                    "generic_data_collection_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_collection_files",
                        to="experiment.mediacollectiondata",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalMediaCollectionData",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.date.today,
                        validators=[
                            experiment.models.validate_date_questionnaire_response
                        ],
                    ),
                ),
                ("time", models.TimeField(blank=True, null=True)),
                ("description", models.TextField()),
                (
                    "file_format_description",
                    models.TextField(blank=True, default="", null=True),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "data_configuration_tree",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="experiment.dataconfigurationtree",
                    ),
                ),
                (
                    "file_format",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="experiment.fileformat",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subject_of_group",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="experiment.subjectofgroup",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical media collection data",
                "verbose_name_plural": "historical media collection datas",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
