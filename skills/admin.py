from django.contrib import admin
from .models import Skill, SkillCategory


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "created_at")
    list_filter = ("level", "categories")
    search_fields = ("name", "description", "contact_name")
