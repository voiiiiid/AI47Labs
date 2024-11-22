from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']



# Login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# CRUD Form
# create
class AddTaskForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['title', 'description']


# update
class UpdateTaskForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['title', 'description']