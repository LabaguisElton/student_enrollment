from django.shortcuts import get_object_or_404, render

from .models import Student

def list_students(request):
	students = Student.objects.all()
	return render(request, "students/student_list.html", {"students": students})

def add_student(request):
	s = Student(first_name="Ana", last_name="Santos", age=22, email="ana@email.com")
	s.save()

	return render(
		request,
		"message.html",
		{"title": "Student Added", "message": "Student Ana added!"},
	)

def delete_student(request, id):
	s = get_object_or_404(Student, id=id)
	s.delete()
	return render(
		request,
		"message.html",
		{"title": "Student Deleted", "message": f"Student {id} deleted."},
	)