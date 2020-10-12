from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/<int:user_id>/create_link/', views.create_link, name='create_link'),

    path('accounts/signup/', views.signup, name='signup'),
]