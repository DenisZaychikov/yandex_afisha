from django.shortcuts import render
from .models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        inner_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_in_detail', args=(place.id,))
            }
        }
        data["features"].append(inner_data)

    context = {'values': data}

    return render(request, 'index.html', context=context)


def place_in_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    data = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }

    return JsonResponse(data,
                        json_dumps_params={'indent': 2, 'ensure_ascii': False})
