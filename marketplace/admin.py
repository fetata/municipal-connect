from django.contrib import admin
from .models import MarketplaceItem, MarketplaceCategory


@admin.register(MarketplaceCategory)
class MarketplaceCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(MarketplaceItem)
class MarketplaceItemAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "condition", "created_at")
    list_filter = ("type", "condition", "category")
    search_fields = ("title", "description")
