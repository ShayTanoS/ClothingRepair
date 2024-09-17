from django.urls import path, include
from django.views.generic import TemplateView
from loginapp.views import LoginView, LoginConfirmView
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(), name='login'),
    path("confirm-code", LoginConfirmView.as_view(), name='confirm_code'),
]