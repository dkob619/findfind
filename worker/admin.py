from django.contrib import admin
from .models import Worker
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
	list_display = ['first_name','Main_job_description', 'City_or_Town']



admin.site.register(Worker, WorkerAdmin)
