from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from places.models import Place
from urllib.parse import unquote

def show_main_page(request):
    features = []
    places = Place.objects.all()

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": '-',
            },
        }
        features.append(feature)

    context = {
        "places": {
            "type": "FeatureCollection",
            "features": features
        }
    }
    return render(request, "index.html", context)


def get_place_json(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {
        "title": place.title,
        "imgs": [unquote(image.img.url) for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lng, "lat": place.lat},
    }
    return JsonResponse(context, json_dumps_params={"ensure_ascii": False, "indent": 4})