from django.db import models


class Registration(models.Model):
	student = models.ForeignKey("students.Student", on_delete=models.CASCADE)
	course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
	registered_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.student} - {self.course}"
