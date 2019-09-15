from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import RevisionForm
from .models import Tool, Revision


class ToolsList(LoginRequiredMixin, ListView):

    template_name = 'tools_list.html'
    # paginate_by = 10
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


class RevisionsList(LoginRequiredMixin, DetailView):

    template_name = 'revision_list.html'
    model = Tool


class CreateTool(LoginRequiredMixin, CreateView):

    template_name = 'addtool.html'
    model = Tool
    fields = ['identifier', 'name', 'location', 'classID']
    success_url = reverse_lazy('tools')

class UpdateTool(LoginRequiredMixin, UpdateView):

    template_name = 'updatetool.html'
    model = Tool
    fields = ['identifier', 'name', 'location', 'classID']
    success_url = reverse_lazy('tools')


class CreateRevision(LoginRequiredMixin, CreateView):

    template_name = 'addrevision.html'
    form_class = RevisionForm
    success_url = reverse_lazy('tools')

    def form_valid(self, form):
        self.object = form.save()
        self.object.tool.pending=False
        self.object.tool.save()
        return redirect(self.get_success_url())

    def get_initial(self):
        initial = super().get_initial()
        init = self.request.GET.get('init')
        if init:
            initial['tool'] = int(init)  # get_object_or_404(Tool, pk=int(init))
        return initial

class SetToolPending(DetailView):

    template_name = 'revision_list.html' 
    model = Tool

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return redirect('/')


    def get_context_data(self,*args,**kwargs):
        data = super().get_context_data(*args,**kwargs)
        data['object'].pending = True
        data['object'].save()

def logout_view(request):
    logout(request)
    return redirect('/')

