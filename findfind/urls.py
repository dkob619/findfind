"""findfind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path
from . import views as site_wide_views
from django.conf import settings 
from django.conf.urls.static import static
from . forms import ContactForm1, ContactForm2, ContactForm3
from . views import ContactWizard


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('worker.urls')),
    url(r'', include('userprofile.urls')),
    url(r'^worker/search/', include('haystack.urls')),


     #User Auth Urls
    url(r'^accounts/login/$', site_wide_views.login, name="login" ),
    url(r'^accounts/auth/$', site_wide_views.auth_view, name="auth_view" ),
    url(r'^accounts/logout/$', site_wide_views.logout, name="logout" ),
    url(r'^accounts/loggedin/$', site_wide_views.loggedin, name="loggedin" ),
    url(r'^accounts/invalid/$', site_wide_views.invalid, name="invalid" ),
    url(r'^accounts/register_user/$', site_wide_views.register_user, name="register_user" ),
    url(r'^accounts/register_success/$', site_wide_views.register_success, name="register_success" ),
    #contact Us
    url(r'^accounts/contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3]), name="contact_us"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
