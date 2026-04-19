from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital', 'experience', 'consultation_fee', 'status', 'created_at')
    list_filter = ('specialization', 'status')
    search_fields = ('name', 'hospital', 'email', 'phone')
    ordering = ('name',)
    list_per_page = 20

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'qualification', 'email', 'phone')
        }),
        ('Professional Details', {
            'fields': ('specialization', 'hospital', 'experience', 'timing', 'consultation_fee')
        }),
        ('Status & Bio', {
            'fields': ('status', 'bio')
        }),
    )

    readonly_fields = ('created_at',)
