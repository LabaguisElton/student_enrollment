from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.list_students, name='list_students'),
	path('add/', views.add_student, name='add_student'),
	path('delete/<int:id>/', views.delete_student, name='delete_student'),
]