from django.shortcuts import render , reverse ,redirect
from django.http import HttpResponse
from connect.models import worker
from master.models import jobs, task
from master.forms import UploadJobForm
from django.db.models import Max
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
import os

def index(request):
    workers=worker.objects.all()
    context={'workers':workers}
    # for session in Session.objects.filter(expire_date__gte=timezone.now()):
    # 	print(session.get_decoded())
    # print("****************")
    # for user in User.objects.all():
    # 	print(user)
    return render(request,'master/master.html',context)

def uploadjob(request):
	if request.method == 'POST':
		if jobs.objects.count()==0:
			jobid=1
		else:
			jobid=jobs.objects.aggregate(Max('id'))['id__max']+1
		form = UploadJobForm(request.POST,request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES.get('file'),jobid,'file.txt')
			handle_uploaded_file(request.FILES.get('process'),jobid,'process.js')
			handle_uploaded_file(request.FILES.get('aggregate'),jobid,'aggregate.js')
			ips=[]
			for session in Session.objects.filter(expire_date__gte=timezone.now()):
				ips.append(session.get_decoded()['ip'])
			validips=worker.objects.filter(worker_ip__in= ips).values_list('id')
			check=[]
			for ip in validips:
				check.append(ip[0])
			print(check)
			splitLen = 65000
			outputBase = 'static/job/'+str(jobid)+'/file'
			input = open(outputBase+'.txt', 'r').read().split('\n')
			at = 1
			slave = 0
			job=jobs()
			job.save()
			for lines in range(0, len(input), splitLen):
			    outputData = input[lines:lines+splitLen]
			    output = open(outputBase + str(at) + '.txt', 'w')
			    output.write('\n'.join(outputData))
			    output.close()
			    newtask = task(taskid = at, jobid=jobid, workerid = check[slave%len(check)])
			    newtask.save()
			    at += 1
			    slave += 1
			return redirect(reverse('master:index'))
	else:
		form = UploadJobForm()
	return render(request,'master/uploadjob.html', {'form': form})

def handle_uploaded_file(f,jobid,fname):
	if not os.path.exists('static/job/'+str(jobid)):
		os.makedirs('static/job/'+str(jobid))
	with open('static/job/'+str(jobid)+'/'+fname, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)