import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.models.fields.files import ImageFieldFile

from ...models import Character


class Command(BaseCommand):
    help = 'Export all Characters to CSV file format'

    def add_arguments(self, parser):
        parser.add_argument('output_file_name', nargs='+', type=str, help='output file name',)

    def handle(self, *args, **options):
        if options['output_file_name']:
            output_file_name = options['output_file_name']
            try:
                with open(output_file_name, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    fields = [f.name for f in Character._meta.get_fields()]
                    writer.writerow(fields)
                    for obj in Character.objects.all():
                        row = []
                        for field in fields:
                            v = getattr(obj, field)
                            if type(v) == ImageFieldFile:
                                row += [v.name]
                            else:
                                row += [v]
                        writer.writerow(row)
            except Character.DoesNotExist:
                raise CommandError('Problem with export')

            self.stdout.write(self.style.SUCCESS('Successfully export to file "%s"' % output_file_name))
