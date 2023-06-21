from django.core.management.base import BaseCommand
from stroer_app.jsonplaceholder.data_sync import forced_sync, add_sync, check_sync


class Command(BaseCommand):
    """Import all Post and Comments linked with JsonPlaceHolder data source.

    Choose a the options: forced, add, or check.

    Example
    -------
    >>> python manage.py sync_jsonplaceholder -p forced
    >>> python manage.py sync_jsonplaceholder -p add
    >>> python manage.py sync_jsonplaceholder -p check
    """
    help = 'Synchronizes the MASTER systems with the JSONPlaceholder API. Choose a the options: forced, add, or check.'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--param', help='Synchronize options [forced, add, check]', )

    def handle(self, *args, **options):
        """API endpoint URLs"""
        param = options['param']
        if param == 'forced':
            forced_sync()
            self.stdout.write('Synch FORCED executed with success!')
        elif param == 'add':
            add_sync()
            self.stdout.write('Synch ADD executed with success!')
        elif param == 'check':
            check_sync()
            self.stdout.write('Synch CHECK executed with success!')
        else:
            self.stdout.write('Synchronize option invalid!')
