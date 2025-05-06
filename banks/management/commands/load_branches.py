import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = 'Loads bank and branch data from CSV file'

    def handle(self, *args, **kwargs):
        with open('bank_branches.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                bank, created = Bank.objects.get_or_create(id=row['bank_id'], defaults={'name': row['bank_name']})

                Branch.objects.update_or_create(
                    ifsc=row['ifsc'],
                    defaults={
                        'bank': bank,
                        'branch': row['branch'],
                        'address': row['address'],
                        'city': row['city'],
                        'district': row['district'],
                        'state': row['state'],
                    }
                )

        self.stdout.write(self.style.SUCCESS('✅ Successfully loaded bank branches from CSV'))
