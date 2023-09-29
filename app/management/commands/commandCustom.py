from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'A custom management command that accepts options and arguments'

    def add_arguments(self, parser):
        parser.add_argument('--greet', type=str, help='Specify a greeting message')
        parser.add_argument('name', type=str, help='Specify a name to greet')

    def handle(self, *args, **options):
        name = options['name']
        greet_message = options['greet'] if options['greet'] else 'Hello'
        self.stdout.write(f'{greet_message}, {name}!')
