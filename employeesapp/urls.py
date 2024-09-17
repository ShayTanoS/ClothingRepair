from django.urls import path, include
from django.views.generic import TemplateView
from employeesapp.views import ProblemsView, HomeView, ListActiveView, ListArchiveView
urlpatterns = [
    path('add-problem', ProblemsView.as_view(), name='add_problem'),
    path('', HomeView.as_view(), name='employees_home'),
    path('list-active', ListActiveView.as_view(), name='list_active'),
    path('list-archive', ListArchiveView.as_view(), name='list_archive'),
]