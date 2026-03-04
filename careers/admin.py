from django.contrib import admin
from .models import JobListing, JobApplication


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'location_type', 'employment_type', 'is_active', 'created_at']
    list_filter = ['department', 'location_type', 'employment_type', 'is_active']
    search_fields = ['title', 'department', 'description']
    list_editable = ['is_active']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'job', 'status', 'applied_at']
    list_filter = ['status', 'job']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['status']
