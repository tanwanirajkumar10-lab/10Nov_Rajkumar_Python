from django.contrib import admin
from .models import Student, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'enrollment_date')
    list_filter = ('enrollment_date',)
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('courses',)
