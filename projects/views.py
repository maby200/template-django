from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Portfolio
from .forms import CreateProjectForm


class ProjectsView(LoginRequiredMixin, TemplateView):
    template_name = 'show_projects/index.html'
    extra_context = {"projects": Portfolio.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['projects'] = Portfolio.objects.all()

        return context
        

class CreateProjectView(LoginRequiredMixin,FormView):
    model = Portfolio
    template_name = 'add_project/index.html'
    form_class = CreateProjectForm

    def form_valid(self, form):
        Portfolio.objects.create(**form.cleaned_data)
        return redirect('index')


@login_required
def deleteProject(request, id):
    project = Portfolio.objects.get(id=id)
    project.delete()
    return redirect('index')