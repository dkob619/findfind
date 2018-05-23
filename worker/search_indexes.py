import datetime
from haystack import indexes
from . models import Worker 


class WorkerIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	date_joined = indexes.DateTimeField(model_attr='date_joined')

	content_auto = indexes.EdgeNgramField(model_attr='Main_job_description')
	#content_auto = indexes.EdgeNgramField(model_attr='City_or_Town')


	def get_model(self):
		return Worker


	def index_queryset(self, using=None):
		#this is used when the entire index for model is updated........
		return self.get_model().objects.all()
		

