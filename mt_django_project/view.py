from django.http import HttpResponse
from mt_django_project.fuelwatch2 import run
from django.shortcuts import render
#def index(request):
#	num = 1
#	return HttpResponse('<p> my favourite number is {} </p?'.format(num))

#from django.shortcuts import render
#def index(request):
	#table = run('Dalkeith')
    
	#return HttpResponse(table)

def index(request):
	
	return render(request,'fuel.html')