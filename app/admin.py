from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'source', 'status', 'last_contact', 'feeling']
    search_fields = ['title', 'description', 'source', 'status', 'feeling']
    list_filter = ['title', 'source', 'status']


admin.site.register(Job, JobAdmin)