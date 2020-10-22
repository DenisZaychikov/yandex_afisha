from django.core.management.base import BaseCommand, CommandError
from place.models import Place, Image
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Load new place'

    def add_arguments(self, parser):
        parser.add_argument('new_filepath', type=str)

    def handle(self, *args, **kwargs):
        filepath = kwargs['new_filepath']

        response = requests.get(filepath)
        response.raise_for_status()
        data = response.json()

        new_place = Place.objects.get_or_create(
            title=data['title'],
            short_description=data['description_short'],
            long_description=data['description_long'],
            lat=data['coordinates']['lat'],
            lon=data['coordinates']['lng']
        )
        new_place.save()

        images_url = data['imgs']
        for index, image_url in enumerate(images_url, 1):
            image_name = image_url.split('/')[-1]
            resp = requests.get(image_url)
            resp.raise_for_status()
            image = resp.content
            new_image = Image.objects.get_or_create(place=new_place,
                                                    image=image_name,
                                                    my_order=index)
            new_image.save()
            new_image.image.save(image_name, ContentFile(image), save=True)
