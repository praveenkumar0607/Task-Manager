from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register,name='register'),
    path('my-login',views.my_login,name='my-login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user-logout',views.user_logout,name='user-logout'),
    path('create-task',views.create_task,name='create-task'),
    path('update-task/<int:pk>',views.update_task,name='update-task'),
    path('task/<int:pk>',views.view_task,name='task'),
    path('delete-task/<int:pk>',views.delete_task,name='delete-task'),
    
]