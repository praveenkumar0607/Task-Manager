from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import task
from django.forms.widgets import PasswordInput, TextInput

# Register user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
# Add Task
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title_task', 'description_task']

# Update Task

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title_task', 'description_task']