from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello,name="hello"),
    path('user_list/',views.Users_list,name="User_list"),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('new_user/', views.new_user, name='new_user'),
    path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]