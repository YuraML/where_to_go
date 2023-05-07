from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import show_main_page, get_place_specs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main_page),
    path('places/<int:place_id>/', get_place_specs, name='place_specs'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
