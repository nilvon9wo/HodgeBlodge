from django.contrib import admin
from FluxHodgeBlodge.jobs.models import Job, Location

class JobAdmin(admin.ModelAdmin):
    list_display = ("job_title", "location", "pub_date")
    ordering = ["-pub_date"]
    search_fields = ("job_title", "job_description")
    list_filter = ("location",)

class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "state", "country")

admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)