from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Worker,Comment
from .forms import WorkerForm,CommentForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.backends import *
from haystack.query import SearchQuerySet


#from django.urls.base import reverse




# Create your views here.
def workers_list(request, id=1):
	workers = Worker.objects.all()
	
	
	return  render(request, 'worker/workers_list.html', {
			
			'workers': workers,
})



def worker_details(request, id):
	worker = get_object_or_404(Worker, id=id)

	return render(request, 'worker/worker_details.html', {
			'worker': worker,

})




def worker_new(request):
	if request.method == 'POST':
		
		form = WorkerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	else:
		form = WorkerForm()
	

	args = {}
	

	args['form'] = form 	

	return render(request, 'worker/worker_new.html', {
		'form': form,
	
})








def worker_add_comment(request, id):
	w = Worker.objects.get(id=id)      

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():              
			c = form.save(commit=False) 
			c.pub_date = timezone.now()
			c.worker = w            
			c.save()                  


			return HttpResponseRedirect('/worker/%s' % id)
	else:
		form = CommentForm()

		#nario = {}

		#nario['worker']= w
		#nario['form']= form



	return render(request, 'worker/worker_add_comment.html', {
		'form':form,
		'w':w,


})


def worker_likes(request, id):
	if id:
		wrk = Worker.objects.get(id=id)
		count = wrk.likes
		count += 1
		wrk.likes = count
		wrk.save()


	return HttpResponseRedirect('/worker/%s' % id)





def worker_search(request):
	workers = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
	return render(request, 'worker/ajax.html', {

		'workers':workers,
		})


'''def worker_search(request):
	workers = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''),


	return render(request, 'worker/ajax_search.html', {
	
		
		'workers':workers,
		


})

    












	#if request.method == "POST":
		#search_region = request.POST['search_region']
		#search_city = request.POST['search_city']
		#search_desc = request.POST['search_desc']
	#else:
		#search_region = ''
		#search_city = ''
		#search_desc = ''

	#worker_region = Worker.objects.filter(Region__contains=search_region)
	#worker_city = Worker.objects.filter(City_or_Town__contains=search_city) 	
	#worker_desc = Worker.objects.filter(Main_job_description__contains=search_desc)#

'''