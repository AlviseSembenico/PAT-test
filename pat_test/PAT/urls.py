from django.urls import path
from .views import ToolsList, CreateTool

urlpatterns = [
    path('tools', ToolsList.as_view()),
    path('addtool', CreateTool.as_view()),
]
