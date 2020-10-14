from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/<int:user_id>/create_link/', views.create_link, name='create_link'),
    path('links/<int:link_id>/', views.link_detail, name='link_detail'),
    path('links/<int:pk>/update/', views.LinkUpdate.as_view(), name='links_update'),
    path('links/<int:pk>/delete/', views.LinkDelete.as_view(), name='links_delete'),
    path('users/<int:user_id>/links/<int:link_id>/notes/', views.CreateNote, name='notes_create'),
    path('links/<int:link_id>/notes/<int:note_id>/delete/', views.DeleteNote, name='notes_delete'),

    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='users_update'),
    path('accounts/signup/', views.signup, name='signup'),
]