from django.http import HttpResponse
from mt_django_project.fuelwatch2 import sortedFuel
from django.shortcuts import render
#def index(request):
#	num = 1
#	return HttpResponse('<p> my favourite number is {} </p?'.format(num))

#from django.shortcuts import render
def index(request):

	product_num = request.GET['product']
	FuelData = sortedFuel('Cannington', product_num)
	
	fuel_data_rows_string = """
        <form>
            <select name="product">
                <option value="1">Unleaded</option>
                option value="2">Premium Unleaded</option>
            </select>
            <button type="submit">Filter</button>
        </form>
    """
	table = run('cannington')
    
	return HttpResponse(table)

#def index(request):
	
#	return render(request,'fuel.html')