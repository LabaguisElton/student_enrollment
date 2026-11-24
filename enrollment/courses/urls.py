from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.list_courses, name="list_courses"),
    path("add/", views.add_course, name="add_course"),
    path("delete/<int:id>/", views.delete_course, name="delete_course"),
]