from django.urls import path
from .views import ToolsList, CreateTool, CreateRevision, RevisionsList, logout_view, SetToolPending, UpdateTool
from .lookup import *

urlpatterns = [
    path('', ToolsList.as_view(), name='tools'),
    path('revisions/<int:pk>', RevisionsList.as_view(), name='revisions'),
    path('addtool', CreateTool.as_view(), name='addtool'),
    path('updatetool/<int:pk>', UpdateTool.as_view(), name='updatetool'),
    path('addrevision', CreateRevision.as_view(), name='addrevision'),
    path('logout', logout_view, name='logout'),
    path('setpending/<int:pk>', SetToolPending.as_view(), name='set_pending')
]
