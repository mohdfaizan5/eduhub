from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:student_id>", views.student, name="student"),
    path("add/", views.add, name="add"),
    path("home", views.home, name="home"),
    path("delete/<int:student_id>", views.delete, name="delete"),
    path("edit/<int:student_id>", views.edit, name="edit"),
    path("contact", views.contact, name="contact"),
    path("notes", views.notes, name="notes")
]
