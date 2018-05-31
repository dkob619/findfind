from django.conf.urls import url, include
from . import views as workerviews
from . api import WorkerResource

worker_resource = WorkerResource()

urlpatterns = [
	url(r'^workers_list$', workerviews.workers_list, name='workers_list'),
	#url(r'^workers_list_user$', workerviews.workers_list_user, name='workers_list_user'),
	url(r'^worker/(?P<id>\d+)/$', workerviews.worker_details, name='worker_details'),
	url(r'^worker/proof_page/(?P<id>\d+)/$', workerviews.worker_proof_page, name='worker_proof_page'),
	url(r'^worker/new/$', workerviews.worker_new, name='worker_new'),
	url(r'^worker_like/(?P<id>\d+)/$', workerviews.worker_like, name='worker_like'),
	url(r'^worker_unlike/(?P<id>\d+)/$', workerviews.worker_unlike, name='worker_unlike'),
	url(r'^worker/add_comment/(?P<id>\d+)/$', workerviews.worker_add_comment, name='worker_add_comment'),
	url(r'^worker/delete_comment/(?P<id>\d+)/$', workerviews.worker_delete_comment, name='worker_delete_comment'),
	url(r'^worker/add_proof/(?P<id>\d+)/$', workerviews.worker_add_proof, name='worker_add_proof'),
	url(r'^worker/search/$', workerviews.worker_search, name="worker_search" ),
	

	url(r'^worker/api/', include(worker_resource.urls)),

	#url(r'^worker_proof_like/(?P<id>\d+)/$', workerviews.worker_proof_like, name='worker_proof_like'),
	#url(r'^worker_proof_unlike/(?P<id>\d+)/$', workerviews.worker_proof_unlike, name='worker_proof_unlike'),

	#url(r'^worker/search_results/$', workerviews.worker_search_results, name="worker_search_results" ),


]
