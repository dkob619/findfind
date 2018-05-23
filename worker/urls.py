from django.conf.urls import url, include
from . import views as workerviews
from . api import WorkerResource

worker_resource = WorkerResource()

urlpatterns = [
	url(r'^$', workerviews.workers_list, name='workers_list'),
	url(r'^worker/(?P<id>\d+)/$', workerviews.worker_details, name='worker_details'),
	url(r'^worker/new/$', workerviews.worker_new, name='worker_new'),
	url(r'^worker_likes/(?P<id>\d+)/$', workerviews.worker_likes, name='worker_likes'),
	url(r'^worker/add_comment/(?P<id>\d+)/$', workerviews.worker_add_comment, name='worker_add_comment'),
	url(r'^worker/search/$', workerviews.worker_search, name="worker_search" ),


	url(r'^worker/api/', include(worker_resource.urls)),





]
