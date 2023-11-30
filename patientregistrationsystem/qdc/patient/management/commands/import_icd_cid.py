import csv
import os
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation.trans_real import activate, deactivate
from patient.models import ClassificationOfDiseases


class Command(BaseCommand):
    help = "Import ICD for translation"

    def add_arguments(self, parser) -> None:
        parser.add_argument("--file", nargs="?", type=str, help="codes filename")

    def handle(self, *args, **options) -> None:
        if options["file"]:
            filename = options["file"]
            try:
                import_classification_of_icd_cid(filename)
            except OSError as exc:
                raise CommandError(f'Filename "{filename}" does not exist.') from exc
            except UnicodeDecodeError as exc:
                raise CommandError(f'Filename "{filename}" has incorrect format.') from exc


def import_classification_of_icd_cid(file_name: str) -> None:
    filename = os.path.join(
        settings.BASE_DIR,
        os.path.join("..", "..", os.path.join("resources", "load-idc-table", file_name)),
    )

    increment = 2  # start of second line, without header

    with open(filename, encoding="utf-8") as csvfile:
        total_lines = sum(1 for _ in csvfile)
    if not total_lines:
        return print("File Empty")

    with open(filename, encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile)
        next(reader, None)
        for row in reader:
            classifications_of_diseases = ClassificationOfDiseases.objects.create(
                code=row[0], description=row[2], abbreviated_description=row[3]
            )

            # colunas _en
            activate("en")
            classifications_of_diseases.description = row[1]
            classifications_of_diseases.abbreviated_description = row[1]
            classifications_of_diseases.save()
            deactivate()
            progress_bar(increment, total_lines, status="Updating database")
            increment += 1
    print("\n")


def progress_bar(count, tot_lines, status="") -> None:
    bar_len = 100

    filled_len = int(round(bar_len * count / float(tot_lines)))

    percents = round(100.0 * count / float(tot_lines), 1)
    bar = "=" * filled_len + "-" * (bar_len - filled_len)

    sys.stdout.write("[{}] {}{} ...{}\r".format(bar, percents, "%", status))
    sys.stdout.flush()
