from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("index", views.index, name="index"),
    path("join", views.join, name="join"),
    path("login", views.login, name="login"),
    path("edit", views.edit, name="edit"),

]



