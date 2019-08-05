from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404

from .forms import RevisionForm
from .models import Tool, Revision


class ToolsList(ListView):

    template_name = 'tools_list.html'
    paginate_by = 10
    model = Tool

    def get_queryset(self):
        p = self.request.GET.get('p') == '1'
        if p:
            return Tool.objects.filter(pending=True)
        else:
            return Tool.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for tool in context["object_list"]:
            tool.last_rev = tool.revision_set.latest('date') if tool.revision_set.count() > 0 else None
            if tool.last_rev:
                tool.last_rev.next_due = tool.last_rev.date.replace(year=tool.last_rev.date.year+1)
        return context


class RevisionsList(DetailView):

    template_name = 'revision_list.html'
    model = Tool


class CreateTool(CreateView):

    template_name = 'addtool.html'
    model = Tool
    fields = ['identifier', 'name']
    success_url = 'tools'


class CreateRevision(FormView):

    template_name = 'addrevision.html'
    form_class = RevisionForm
    success_url = 'tools'

    def get_initial(self):
        initial = super().get_initial()
        init = self.request.GET.get('init')
        if init:
            initial['tool'] = int(init)  # get_object_or_404(Tool, pk=int(init))
        return initial
