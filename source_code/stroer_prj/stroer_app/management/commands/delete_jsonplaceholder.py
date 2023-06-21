from django.core.management.base import BaseCommand

from stroer_app.jsonplaceholder.data_exists import exists_jsonplaceholder
from stroer_app.jsonplaceholder.data_delete import delete_jsonplaceholder


class Command(BaseCommand):
    """Delete all Post and Comments linked with JsonPlaceHolder data source.

    Example
    -------
    >>> python manage.py delete_jsonplaceholder
    """
    help = 'Delete all data imported from the JSONPlaceholder API.'

    def handle(self, *args, **options):
        """API endpoint URLs"""
        if exists_jsonplaceholder():
            delete_jsonplaceholder()
            self.stdout.write('JSONPlaceholder was deleted successfully!')
        else:
            self.stdout.write('JSONPlaceholder data not exists!')
