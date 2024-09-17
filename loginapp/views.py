from django.shortcuts import render, redirect
from django.views import View
from .forms import TelegramForm, ConfirmCodeForm
from .functions import send_message_to_username
from random import randint
from .models import User
from django.contrib.auth import login, authenticate
# Create your views here.

class LoginView(View):
    template_name = 'login/login.html'
    def get(self, request):
        form = TelegramForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = TelegramForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['telegram_login']
            request.session['code'] = randint(1000,9999)
            result = send_message_to_username(request.session['username'], f'Код підтвердження:\n{request.session['code']}')
            print(result)
            if result:
                request.session['id'] = result
                return redirect("confirm_code")
        return render(request, self.template_name, {'form': form, 'message': "Або ви не активували бота, або некоректний username"})

def check_record_exists(id):
    try:
        User.objects.get(user_id=id)
        return True
    except:
        return False

class LoginConfirmView(View):
    template_name = 'login/confirm_code.html'
    def get(self, request):
        form = ConfirmCodeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ConfirmCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if request.session['code'] == code:
                if not check_record_exists(request.session['id']):
                    user = User.objects.create(user_id=request.session['id'], username=request.session["username"])
                else:
                    user = User.objects.get(username=request.session['username'])
                login(request, user)
                print(user.is_staff, user.is_superuser)
                if user.is_staff or user.is_superuser:
                    return redirect('employees_home')
                else:
                    return redirect('home')
            request.session['code'] = randint(1000, 9999)
            send_message_to_username(request.session['username'], f'Код підтвердження:\n{request.session['code']}')
            return render(request, self.template_name, {'form': form, 'message': "Неправильний код, відправлено новий"})
        return render(request, self.template_name, {'form': form})

