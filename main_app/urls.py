from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users/<int:user_id>/create_link/', views.create_link, name='create_link'),
    path('links/<int:link_id>/', views.link_detail, name='link_detail'),
    path('links/<int:pk>/update/', views.LinkUpdate.as_view(), name='links_update'),
    # path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]