from django.shortcuts import render
from places.models import Place


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
