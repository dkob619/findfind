from django import forms
from . models import UserProfile



class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('likes_this_site','favourite_worker_name')