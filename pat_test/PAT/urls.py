from django.urls import path
from .views import ToolsList

urlpatterns = [
    path('tools', ToolsList.as_view()),
]
