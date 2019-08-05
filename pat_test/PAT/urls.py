from django.urls import path
from .views import ToolsList, CreateTool, CreateRevision, RevisionsList
from .lookup import *

urlpatterns = [
    path('', ToolsList.as_view()),
    path('revisions/<int:pk>', RevisionsList.as_view()),
    path('addtool', CreateTool.as_view()),
    path('addrevision', CreateRevision.as_view()),
]
