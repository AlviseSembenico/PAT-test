from django.contrib import admin
from .models import Tool, Revision


@admin.register(Tool)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name']


@admin.register(Revision)
class ToolsAdmin(admin.ModelAdmin):
    list_display = [
        'tool',
        'date',
        'test_engineer',
        'pending'
    ]
