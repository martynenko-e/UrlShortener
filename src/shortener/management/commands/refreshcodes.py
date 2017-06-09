from django.core.management.base import BaseCommand
from shortener.models import ShortUrl


class Command(BaseCommand):
    help = 'Refreshes all ShortUrl shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items',  type=int)

    def handle(self, *args, **options):
        print "You try to refresh codes start from {i}".format(i=options['items'])






