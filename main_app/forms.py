from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Link


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'avatar')

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ('address', 'title', 'link_type', 'tags', 'created_date', 'planned_date', 'viewed_date', 'github_project', 'code_snippet', 'status')