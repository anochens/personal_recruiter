# myapp/management/commands/insert_jobs_from_csv.py
import csv
from django.core.management.base import BaseCommand
from app.models import Job, FeelingChoice

class Command(BaseCommand):
    help = 'Inserts many records into the Job model from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        job, _ = Job.objects.get_or_create(
                            title=row['title'],
                            description=row['description'],
                            source=row['source'],
                            last_contact=None if not row['last_contact'] else row['last_contact'],
                            feeling=FeelingChoice[row['feeling'].upper()],
                        )
                        self.stdout.write(self.style.SUCCESS(f'Successfully inserted record: {job}'))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'An error occurred with record: {row}, Error: {e}'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'CSV file {csv_file} not found.'))


