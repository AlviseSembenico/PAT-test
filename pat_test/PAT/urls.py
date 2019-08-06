from django.urls import path
from .views import ToolsList, CreateTool, CreateRevision, RevisionsList
from .lookup import *

urlpatterns = [
    path('', ToolsList.as_view(), name='tools'),
    path('revisions/<int:pk>', RevisionsList.as_view(), name='revisions'),
    path('addtool', CreateTool.as_view(), name='addtool'),
    path('addrevision', CreateRevision.as_view(), name='addrevision'),
]
