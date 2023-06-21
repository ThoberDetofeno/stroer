from django.core.management.base import BaseCommand

from stroer_app.jsonplaceholder.data_import import import_jsonplaceholder
from stroer_app.jsonplaceholder.data_exists import exists_jsonplaceholder


class Command(BaseCommand):
    """Import all Post and Comments linked with JsonPlaceHolder data source.

    Example
    -------
    >>> python manage.py import_jsonplaceholder
    """
    help = 'Import posts and comments from JSONPlaceholder API.'

    def handle(self, *args, **options):
        """API endpoint URLs"""
        if exists_jsonplaceholder():
            self.stdout.write('Data already imported!')
        else:
            if import_jsonplaceholder():
                self.stdout.write('Successfully imported JsonPlaceHolder data!')
            else:
                self.stdout.write('Internal server error!')
