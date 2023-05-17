import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places from JSON files'

    def get_images(self, place, links):
        for number, link in enumerate(links):
            image_name = link.split('/')[-1]
            response = requests.get(link)
            response.raise_for_status()
            img = ContentFile(response.content, name=image_name)
            Image.objects.create(place=place, img=img, number=number)

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='JSON file url')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        place_meta = response.json()
        img_links = place_meta.get('imgs', [])

        place, created = Place.objects.get_or_create(
            title=place_meta['title'],
            defaults={
                'description_short': place_meta.get('description_short', ''),
                'description_long': place_meta.get('description_long', ''),
                'lng': place_meta['coordinates']['lng'],
                'lat': place_meta['coordinates']['lat'],
            }
        )

        if created:
            self.get_images(place, img_links)
