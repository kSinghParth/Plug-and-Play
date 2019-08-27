from django.shortcuts import render , reverse ,redirect
from django.http import HttpResponse
from connect.models import worker
from master.models import jobs
from master.forms import UploadJobForm
from django.db.models import Max
import os

def index(request):
    workers=worker.objects.all()
    context={'workers':workers}
    return render(request,'master/master.html',context)

def uploadjob(request):
	if request.method == 'POST':
		if jobs.objects.count()==0:
			jobid=1
		else:
			jobid=jobs.objects.aggregate(Max('id'))['id__max']+1
		form = UploadJobForm(request.POST,request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES.get('process'),jobid,'process.js')
			handle_uploaded_file(request.FILES.get('aggregate'),jobid,'aggregate.js')
			job=jobs()
			job.save()
			return redirect(reverse('master:index'))
	else:
		form = UploadJobForm()
	return render(request,'master/uploadjob.html', {'form': form})

def handle_uploaded_file(f,jobid,fname):
	if not os.path.exists('media/job/'+str(jobid)):
		os.makedirs('media/job/'+str(jobid))
	with open('media/job/'+str(jobid)+'/'+fname, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)