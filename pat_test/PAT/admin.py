from django.contrib import admin
from .models import Tool, Revision


@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = [
        'identifier',
        'name',
        'pending',
    ]


@admin.register(Revision)
class RevisionAdmin(admin.ModelAdmin):

    list_display = [f.name for f in Revision._meta.fields]
