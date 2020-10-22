from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" />'.format(
                url=obj.image.url,
                width=200,
            )
        )


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    inlines = [
        ImageInLine,
    ]
