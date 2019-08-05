from django.urls import path
from .views import ToolsList, CreateTool, CreateRevision
from .lookup import *

urlpatterns = [
    path('tools', ToolsList.as_view()),
    path('addtool', CreateTool.as_view()),
    path('addrevision', CreateRevision.as_view()),
]
