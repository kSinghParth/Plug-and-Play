from django.shortcuts import render , reverse ,redirect
from django.http import HttpResponse
from connect.models import worker
from master.models import textJob
from master.forms import NameForm

def index(request):
    workers=worker.objects.all()
    context={'workers':workers}
    return render(request,'master/master.html',context)

def uploadjob(request):
	if request.method == 'POST':
		form = NameForm(request.POST,request.FILES)
		if form.is_valid():
			# handle_uploaded_file(request.FILES['file'])
			newdoc = textJob(docfile = request.FILES.get('process'))
			newdoc.save()
			return HttpResponse('/thanks/')
	else:
		form = NameForm()
	return render(request,'master/uploadjob.html', {'form': form})

def addtext(request):
	if request.method == 'POST':
		text= request.POST['text']
		newtext = textJob(text=text)    
		newtext.save()
	return render(request,'master/addtext.html')	

def handle_uploaded_file(f):
    with open('media/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)