from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Tool, Revision


class ToolsList(ListView):

    template_name = 'tools_list.html'
    paginate_by = 10
    model = Tool

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for tool in context["object_list"]:
            tool.pass_date = tool.revision_set.latest('date').date if tool.revision_set.count() > 0 else None
        return context
