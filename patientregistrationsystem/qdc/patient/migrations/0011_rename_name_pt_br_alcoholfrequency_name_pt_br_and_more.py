# Generated by Django 4.2.4 on 2023-08-15 03:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0010_alter_medicalrecorddata_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="alcoholfrequency",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="alcoholperiod",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="amountcigarettes",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="classificationofdiseases",
            old_name="abbreviated_description_pt_br",
            new_name="abbreviated_description_pt_br",
        ),
        migrations.RenameField(
            model_name="classificationofdiseases",
            old_name="description_pt_br",
            new_name="description_pt_br",
        ),
        migrations.RenameField(
            model_name="fleshtone",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="gender",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="maritalstatus",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="payment",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="religion",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
        migrations.RenameField(
            model_name="schooling",
            old_name="name_pt_br",
            new_name="name_pt_br",
        ),
    ]
