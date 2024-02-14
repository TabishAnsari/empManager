from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit", views.edit, name="edit"),
    path("search", views.search, name="search"),
    path("create",views.create, name="create"),
    path("delete", views.delete, name="delete"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
]