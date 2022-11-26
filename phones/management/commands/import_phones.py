import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
        '-import_data', 
        action='store_true', 
        default=False,
        help='Перенести данные из csv-файла в БД'
        )

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                name=phone['name'], 
                image=phone['image'], 
                price=phone['price'], 
                release_date=phone['release_date'], 
                lte_exists=phone['lte_exists'], 
            )
