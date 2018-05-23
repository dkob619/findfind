from django import forms
from . models import Worker, Comment





class WorkerForm(forms.ModelForm):

	class Meta:
		model = Worker
		fields = ('first_name', 'last_name', 'age','gender',
			'Call_Number', 'WhatsApp', 'Main_job_description',
            'Other_jobs_description', 
			'Region', 'City_or_Town', 'bio',
            'profile_Picture',
            )





class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('name','message')
