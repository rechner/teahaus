from django.contrib import admin

from .models import Tea
from .models import TeaType


@admin.register(TeaType)
class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "temperature")
    search_fields = ("name",)


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "barcode", "in_stock", "notes")
    list_filter = ("type",)
    search_fields = ("name",)
