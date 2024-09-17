from django.shortcuts import render
from django.views import View
from .forms import ProblemForm
from .models import ActiveProblem, Problem
from django.views.generic import TemplateView


class ProblemsView(View):
    template_name = 'employees/add_problems.html'

    def get(self, request):
        form = ProblemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save()
            ActiveProblem.objects.create(problem=problem)
        return render(request, self.template_name, {'form': form})


class HomeView(View):
    template_name = 'employees/home.html'

    def get(self, request):
        context = {'problems': ActiveProblem.objects.all()}
        return render(request, self.template_name, context)


class ListActiveView(View):
    template_name = 'employees/list_active.html'

    def get(self, request):
        context = {'problems': ActiveProblem.objects.all()}
        return render(request, self.template_name, context)


class ListArchiveView(View):
    template_name = 'employees/list_archive.html'

    def get(self, request):
        context = {'problems': Problem.objects.all()}
        return render(request, self.template_name, context)
