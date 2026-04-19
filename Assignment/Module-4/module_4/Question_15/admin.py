from django.contrib import admin

from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'availability', 'experience_years', 'phone', 'email')
    list_filter = ('specialty', 'availability')
    search_fields = ('name', 'specialty', 'phone')
    list_per_page = 20
    ordering = ('name',)
