from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import UserProfileForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required #this checks to see whether the user is logged in or redirects to the login page.
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/loggedin')

	else:
		user = request.user
		profile = user.profile
		form = UserProfileForm(instance=profile)

	return render(request, 'userprofile/profile.html', {
			'form':form,

			})
