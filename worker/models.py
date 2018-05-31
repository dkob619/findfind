from django.db import models
from django.utils import timezone
from findfind import settings 
import datetime
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class Worker(models.Model):


    
	greater_accra_region = 'GA'
	central_region = 'CR'
	western_region =  'WR'
	eastern_region = 'ER'
	volta_region = 'VR'
	ashanti_region = 'AS'
	brong_ahafo_region = 'BA' 
	northern_region = 'NR'
	upper_east_region = 'UE'
	upper_west_region = 'UW'

	regions_in_ghana_choices = (
		(greater_accra_region, 'Greater Accra Region'),
		(central_region, 'Central Region'),
		(western_region, 'Western Region'),
		(eastern_region, 'Eastern Region'),
		(volta_region, 'Volta Region'),
		(ashanti_region, 'Ashanti Region'),
		(brong_ahafo_region, 'Brong Ahafo Region'),
		(northern_region, 'Northern Region'),
		(upper_east_region, 'Upper East Region'),
		(upper_west_region, 'Upper West Region'),

		)
	
	male =  'M'
	female = 'F'

	gender_choices =(
		(male, 'Male'),
		(female, 'Female'),
		)







	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField(default=18)	
	gender = models.CharField(max_length=1, choices=gender_choices, default=male)
	Call_Number = models.CharField(max_length=10, help_text='*REQUIRED*')
	WhatsApp  = models.CharField(max_length=10, blank=True, help_text='Ignore If Call number is the same for WhatsApp')
	Main_job_description = models.CharField(max_length=30, help_text='e.g Carpenter' )
	Other_jobs_description = models.CharField(max_length=50, blank=True)
	Region = models.CharField(max_length=2, choices=regions_in_ghana_choices, default=greater_accra_region)
	City_or_Town = models.CharField(max_length=50)
	bio = models.TextField()
	profile_Picture = models.FileField(upload_to=get_upload_file_name)
	date_joined = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)

	

	def __unicode__(self):
		return self.first_name + '   >>> ' +self.main_job_description
	

	def get_absolute_url(self):
		return 'worker/%i' % self.id

	def get_profile_picture(self):

		profile_pic = str(self.profile_picture)
		if not settings.DEBUG:
			profile_pic = profile_pic.replace('assets/', '')

		return profile_pic








class Comment(models.Model):
	name = models.CharField(max_length=50)
	message = models.TextField()
	pub_date = models.DateTimeField('Date Publised')
	worker = models.ForeignKey('Worker', on_delete=models.CASCADE)



class Proof(models.Model):
	image_description = models.CharField(max_length=100)
	image = models.FileField(upload_to=get_upload_file_name)
	likes = models.IntegerField(default=0)
	posted_on = models.DateTimeField('Date Posted')
	worker = models.ForeignKey('Worker', on_delete=models.CASCADE)


	def get_profile_picture(self):
		image = str(self.image)
		if not settings.DEBUG:
			image = image.replace('assets/', '')

		return image





            

            
