from django import template
import os

register = template.Library()

@register.simple_tag
def storeresult(context,arg,cad):
	print(cad)
	if not os.path.exists('static/job/'+str(context)):
		os.makedirs('static/job/'+str(context))
	f= open("static/job/"+str(context)+"/output"+str(arg)+".txt","w+")
	f.write("balle balle")
	f.close()
	return cad