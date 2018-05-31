from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	surname = forms.CharField(required=True)
	email = forms.EmailField(required=True)


	class Meta: 
		model = User
		fields =('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['surname']
		user.email = self.cleaned_data['email']

		user.set_password(self.cleaned_data["password1"])
		
		if commit:
			user.save()
		return user





class ContactForm1(forms.Form):
	full_name = forms.CharField(max_length=50)


class ContactForm2(forms.Form):
	phone = forms.CharField(max_length=10)


class ContactForm3(forms.Form):
	email = forms.EmailField()





