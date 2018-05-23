from django.conf.urls import url, include
from . import views as userprofileViews



urlpatterns = [
	url(r'^accounts/profile/$', userprofileViews.user_profile, name='user_profile'),





]
