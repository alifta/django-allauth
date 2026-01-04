from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("secret/", views.secret, name="secret"),
    path("todo/", views.todo, name="todo"),
    path("submit-todo/", views.submit_todo, name="submit-todo"),
    path("complete-todo/<int:todo_id>/", views.complete_todo, name="complete-todo"),
    path("delete-todo/<int:todo_id>/", views.delete_todo, name="delete-todo"),
]
