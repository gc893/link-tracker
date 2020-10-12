from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Link
from django.contrib.auth import login
from .forms import CustomUserCreationForm, LinkForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def create_link(request, user_id):
  error_message = ''
  if request.method == 'POST':
    form = LinkForm(request.POST)

    if form.is_valid():
        new_link = form.save(commit=False)
        new_link.user_id = user_id
        new_link.save()
        return redirect('dashboard')

    else:
        print(form.errors)
        error_message = 'Invalid sign up - try again'

  form = LinkForm()
  context = {'link_form': form, 'error_message': error_message}
  return render(request, 'main_app/link_form.html', context)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('dashboard')
    else:
      print(form.errors)
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = CustomUserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)