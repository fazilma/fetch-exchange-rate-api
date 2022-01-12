from django.core.management.base import BaseCommand

from apirate.coinMena.fetch_rate import fetch_rate

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    def handle(self, *args, **options):
        
        return fetch_rate()