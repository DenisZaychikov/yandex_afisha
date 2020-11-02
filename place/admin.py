from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

IMAGE_WIDTH = 200


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    readonly_fields = ["get_preview"]
    raw_id_fields = ['place']

    def get_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}" />', obj.image.url, IMAGE_WIDTH
        )


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html(
            '<img src="{}" width="{}" />', obj.image.url, IMAGE_WIDTH
        )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]
