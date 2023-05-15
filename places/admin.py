from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    raw_id_fields = ("place",)
    readonly_fields = ["get_preview"]

    def get_preview(self, img):
        return format_html(
            '<img src="{}" style="max-width:{};max-height:{};width:{};height:{};" />',
            img.img.url,
            "200px",
            "200px",
            "auto",
            "auto",
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["title"]
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["img"]
