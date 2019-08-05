from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Tools, Revision


class ToolsList(ListView):

    template_name = 'tools_list.html'
    paginate_by = 10
    model = Tools
