from django.urls import path
from . import views

urlpatterns = [
	path("list/", views.list_registrations, name="list_registrations"),
	path(
		"add/<int:student_id>/<int:course_id>/",
		views.add_registration,
		name="add_registration",
	),
	path("delete/<int:id>/", views.delete_registration, name="delete_registration"),
]