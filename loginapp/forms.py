from django import forms

class TelegramForm(forms.Form):
    telegram_login = forms.CharField(label='Telegram Login', max_length=100)

class ConfirmCodeForm(forms.Form):
    code = forms.IntegerField(label='Confirm Code')