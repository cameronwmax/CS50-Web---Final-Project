from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_list", views.create_list, name="create_list"),
    path("my_list", views.my_list, name="my_list"),
    path("delete_list/<int:list_id>", views.delete_list, name="delete_list"),
    path("delete_all", views.delete_all, name="delete_all"),
    path("edit_task/<int:list_id>", views.edit_task, name="edit_task"),
]