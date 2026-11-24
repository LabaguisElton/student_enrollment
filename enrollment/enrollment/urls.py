from django.contrib import admin
from django.urls import path, include  # <--- Add "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # <--- Add this line
    path('courses/', include('courses.urls')), # <--- Add this line
    path('registrations/', include('registrations.urls')), # <--- Add this line
]