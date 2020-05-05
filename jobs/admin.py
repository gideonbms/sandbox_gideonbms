from django.contrib import admin
from .models import *

class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'experience', 'education', 'location')
    list_filter = ('experience', 'education', 'location')

admin.site.register(Contact)
admin.site.register(JobListing)
admin.site.register(ApplyJob, ApplyJobAdmin)

