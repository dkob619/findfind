from tastypie.resources import ModelResource
from tastypie.constants import ALL
from . models import Worker


class WorkerResource(ModelResource):
	class Meta:
		queryset = Worker.objects.all()
		resource_name = 'worker'
		filtering = {"Main_job_description" : ALL}
