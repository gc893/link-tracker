from django.shortcuts import render, redirect
from django.views.generic import DetailView , ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Link, User, Note
from django.contrib.auth import login
from .forms import CustomUserCreationForm, LinkForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

# Create your views here.

def home(request):
    return render(request, 'home.html')

class Search(ListView):
    model = Link

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'today': date.today()})

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

@login_required
def link_detail(request, link_id):
    positives = 0
    negatives = 0
    questions = 0
    link = Link.objects.get(id=link_id)
    note_form = NoteForm()
    notes = Note.objects.filter(link=link_id)
    for note in notes:
        if note.note_type == 'p':
            positives += 1
        elif note.note_type == 'n':
            negatives += 1
        else:
            questions += 1
    return render(request, 'main_app/detail.html', {'link': link, 'note_form': note_form, 'possitives': positives, 'negatives': negatives, 'questions': questions})

class LinkUpdate(LoginRequiredMixin, UpdateView):
    model = Link
    fields = ('address', 'title', 'link_type', 'tags', 'created_date', 'planned_date', 'viewed_date', 'github_project', 'code_snippet', 'status')
    success_url = '/dashboard/'

class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = '/dashboard'

@login_required
def CreateNote(request, user_id, link_id):
  # create a ModelForm instance using the data in request.POST
  form = NoteForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_note = form.save(commit=False)
    new_note.user_id = user_id
    new_note.link_id = link_id
    new_note.save()
  return redirect('link_detail', link_id=link_id)

@login_required
def DeleteNote(request,link_id, note_id):
    Note.objects.filter(id= note_id).delete()
    success_url = f'/links/{link_id}'
    return redirect(success_url)

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

class UserUpdate(LoginRequiredMixin, UpdateView):
  model = User
  fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
  success_url = '/dashboard'