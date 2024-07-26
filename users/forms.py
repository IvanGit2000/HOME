from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User



class UserLoginform(AuthenticationForm):    

    class Meta:
        model = User
        fields = ["username", "password"]
    
    username = forms.CharField()
    password = forms.CharField()



    
# class UserLoginform(AuthenticationForm):    

#     username = forms.CharField(
#         label= 'Логін',
#         widget=forms.TimeInput(
#             attrs={
#                 "autofocus": True,
#                 "class": "form-control",
#                 "placeholder": "Введите ваше имя пользователя",
#             }
#         )
#     )
#     password = forms.CharField(
#         label= 'Пароль',
#         widget=forms.PasswordInput(
#             attrs={
#                 "autocomplete": "current-password",
#                 "class": "form-control",
#                 "placeholder": "Введите ваш пароль",
#             }
#         )
#     )

#     class Meta:
#         model = User
#         fields = ["username", "password"]
