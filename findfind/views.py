from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms
from . forms import MyRegistrationForm
from django.contrib import auth
from django.contrib import messages 
from django.contrib.auth.models import User

#django formtools 
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import logging
logr = logging.getLogger(__name__)



#from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm



def login(request):
	c = {}

	return render(request, 'accounts/login.html', {
		'c': c,

})


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)


	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')

	else:
		return HttpResponseRedirect('/accounts/invalid')




def loggedin(request):
	return render(request, 'accounts/loggedin.html', {
		'username': request.user.username,
		'firstname': request.user.first_name,
		'surname': request.user.last_name,
		'email': request.user.email,

})


def invalid(request):
	return render(request, 'accounts/invalid.html', {

})

def logout(request):
	auth.logout(request)


	return render(request, 'accounts/logout.html', {

})


def register_user(request):
	if request.method == "POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account was created Successfully!')
			return HttpResponseRedirect('/accounts/register_success')

	else:

		form = MyRegistrationForm()

	return render(request, 'accounts/register_user.html', {

		'form': form,
})	





def register_success(request):
	return render(request, 'accounts/register_success.html', {


})



#The Contact Wizard View, Which is actually Class-Based..
class ContactWizard(SessionWizardView):
	template_name = "accounts/contact_form.html"



	def done(self, form_list, **kwds):
		form_data = process_form_data(form_list)

		return render(request, 'accounts/done.html', {
			'form_data': form_data,

			})


def process_form_data(form_list):
	form_data = [form for form in form_list]

	#logr.debug(form_data[0]['full_name'])
	#logr.debug(form_data[1]['contact'])
	#logr.debug(form_data[2]['email'])


	send_mail(
		form_data[0]['full_name'],
		form_data[1]['contact'],
		form_data[2]['email'],

		['dkob619@gmail.com'],
		fail_silently=False

		)

	return form_data


