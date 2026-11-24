from django.shortcuts import get_object_or_404, render

from .models import Course


def list_courses(request):
	courses = Course.objects.all()
	return render(request, "courses/course_list.html", {"courses": courses})


def add_course(request):
	course = Course(
		name="Python Fundamentals",
		description="An introduction to Python programming.",
		instructor="Alex Morgan",
		duration=8,
	)
	course.save()
	return render(
		request,
		"message.html",
		{"title": "Course Added", "message": f"Course {course.name} added!"},
	)


def delete_course(request, id):
	course = get_object_or_404(Course, id=id)
	course.delete()
	return render(
		request,
		"message.html",
		{"title": "Course Deleted", "message": f"Course {id} deleted."},
	)