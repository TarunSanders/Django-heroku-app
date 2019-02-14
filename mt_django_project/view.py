from django.http import HttpResponse
from mt_django_project.fuelwatch2 import sortedFuel, createfuelHTMLTABLE
from django.shortcuts import render
#def index(request):
#	num = 1
#	return HttpResponse('<p> my favourite number is {} </p?'.format(num))

#from django.shortcuts import render
def index(request):

	product_num = request.GET.get('product')
	
	suburbAndsurrounding = request.GET.get('suburb')
	

	FuelData = sortedFuel(suburbAndsurrounding,product_num)
	"""
	fuel_data_rows_string = """
        <form>
			<select name = "product">
				<option value = "1"> Unleaded </option>
				<option value = "2"> Premium Unleaded </option>
				<option value = "3"> Diesel </option>
				<option value = "4"> LPG </option>
				<option value = "5"> Branded Diesel </option>
			
			</select>

            Suburb and surrounding (defaults to all metro regions in WA): <input type="text" name="suburb">
  			<button type="submit"> Enter </button> 
		</form>
		"""
    """
	#Suburb (type 'metro' for all metro regions): <input type="text" name="suburb">
  	#		<button type="submit"> Enter </button> 
	
	fuel_data_rows_string = "<html><body>" + fuel_data_rows_string + createfuelHTMLTABLE(FuelData)+"</body></html>"
    
	return HttpResponse(fuel_data_rows_string)

#def index(request):
	
#	return render(request,'fuel.html') 