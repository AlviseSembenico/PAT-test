from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Tool, Revision


class ToolsList(ListView):

    template_name = 'tools_list.html'
    paginate_by = 10
    model = Tool

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for tool in context["object_list"]:
            tool.last_rev = tool.revision_set.latest('date') if tool.revision_set.count() > 0 else None
            if tool.last_rev:
                tool.last_rev.next_due = tool.last_rev.date.replace(year=tool.last_rev.date.year+1)
        return context


class CreateTool(CreateView):

    template_name = 'addtool.html'
    model = Tool
    fields = ['identifier', 'name']
    success_url = 'tools'
