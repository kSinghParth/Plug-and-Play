from django.shortcuts import render , reverse ,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
import os
from django.utils.encoding import smart_str
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from background_task import background
import time
from connect.models import worker
from master.models import task
from django.utils import timezone


def index(request):
    return redirect(reverse('connect:login'))

def login(request):
	if request.method == 'POST':
		password= request.POST['password']
		
		if password=="abc":
			x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
			ip = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forward_for:
				ip = x_forward_for.split(',')[0]
			else:
			    ip = request.META.get('REMOTE_ADDR')
			request.session['ip'] = ip
			worker_node = worker(worker_ip=request.session['ip'],last_ping=timezone.now() , status=1)    
			worker_node.save()
			return redirect(reverse('connect:dashboard'))  
		else:
			messages.add_message(request, messages.ERROR, 'Invalid password')
			return render(request,'connect/login.html')	
	else:
		return render(request,'connect/login.html')	
			

def dashboard(request):
	if request.session['ip']:
		redirect(reverse('connect:login'))
	return render(request,'connect/dashboard.html')

def process(request):
	if request.session['ip']:
		redirect(reverse('connect:login'))
	id=worker.objects.filter(worker_ip=request.session['ip']).values_list('id')[0][0]
	tasks=task.objects.filter(workerid=id).values_list('taskid','jobid','id')
	param={}
	param['jobid']=str(tasks[0][1])
	param['tasks']=[]
	for t in tasks:
		obj = task.objects.filter(id=t[2]).update(status=1)
		details = {}
		details['taskid']=str(t[0])
		f = open('static/job/'+str(param['jobid'])+'/file'+str(t[0])+'.txt', 'r')
		file_content = f.read()
		f.close()
		details['content']=file_content.replace('\n',' ')
		details['tid']=t[2]
		param['tasks'].append(details)
	return render(request,'connect/process.html',param)


def storeresult(request):
	jobid = request.GET.get('jobid', None)
	taskid = request.GET.get('taskid', None)
	tid = request.GET.get('tid', None)
	content = request.GET.get('content', None)
	obj = task.objects.filter(id=tid).update(status=2)
	if not os.path.exists('static/job/'+str(jobid)):
		os.makedirs('static/job/'+str(jobid))
	f= open("static/job/"+str(jobid)+"/output"+str(taskid)+".txt","w+")
	f.write(str(content))
	f.close()
	data = {
	'taken':True}
	return JsonResponse(data);

def logout_view(request):
	worker.objects.filter(worker_ip=request.session['ip']).delete()
	logout(request)
	return redirect(reverse('connect:login'))

@background(schedule=3)
def check(ip):
	# print(ip+"   "+time.ctime())
	print("hello")
