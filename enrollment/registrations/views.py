from django.shortcuts import get_object_or_404, render

from courses.models import Course
from students.models import Student

from .models import Registration


def list_registrations(request):
	registrations = Registration.objects.select_related("student", "course")
	return render(
		request,
		"registrations/registration_list.html",
		{"registrations": registrations},
	)


def add_registration(request, student_id, course_id):
	student = get_object_or_404(Student, id=student_id)
	course = get_object_or_404(Course, id=course_id)
	_, created = Registration.objects.get_or_create(
		student=student,
		course=course,
	)
	message = "Registration added!" if created else "Registration already exists."
	return render(
		request,
		"message.html",
		{"title": "Registration", "message": message},
	)


def delete_registration(request, id):
	registration = get_object_or_404(Registration, id=id)
	registration.delete()
	return render(
		request,
		"message.html",
		{"title": "Registration Deleted", "message": f"Registration {id} deleted."},
	)