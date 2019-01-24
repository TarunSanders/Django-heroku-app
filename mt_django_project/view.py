from django.http import HttpResponse
from mt_django_project.fuelwatch2 import run
from django.shortcuts import render
#def index(request):
#	num = 1
#	return HttpResponse('<p> my favourite number is {} </p?'.format(num))

#from django.shortcuts import render
def index(request):

	#suburb_chosen = request.GET['suburb']
	
	table = run(suburb_chosen)
    
	return HttpResponse(table)

#def index(request):
	
#	return render(request,'fuel.html')