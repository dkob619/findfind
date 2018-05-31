from django.contrib import admin
from .models import Worker, Comment, Proof
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
	list_display = ['first_name','Main_job_description', 'City_or_Town']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name','message']


class ProofAdmin(admin.ModelAdmin):
	list_display = ['image_description']

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Proof, ProofAdmin)

