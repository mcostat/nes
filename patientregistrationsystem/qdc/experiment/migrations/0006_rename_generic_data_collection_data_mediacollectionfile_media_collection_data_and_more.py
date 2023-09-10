# Generated by Django 4.2.5 on 2023-09-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "experiment",
            "0005_informationtypemedia_alter_component_component_type_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="mediacollectionfile",
            old_name="generic_data_collection_data",
            new_name="media_collection_data",
        ),
        migrations.AlterField(
            model_name="fileformat",
            name="extension",
            field=models.CharField(max_length=100),
        ),
    ]
