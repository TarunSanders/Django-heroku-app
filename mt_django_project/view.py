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
	
	fuel_data_rows_string = """
        <form autocomplete="on">
			<select name = "product" autocomplete="on">
				<option value = "1" {unl} > Unleaded </option>
				<option value = "2" {prem} > Premium Unleaded </option>
				<option value = "3"{dies} > Diesel </option>
				<option value = "4" {l} > LPG </option>
				<option value = "5" {bd}> Branded Diesel </option>
			
			</select>

            Suburb and surrounding (type 'metro' for all metro regions): <input type="text" name="suburb" value ="{s}">
  			<button type="submit"> Enter </button> 
		</form>
    """.format(unl = 'selected' if product_num == '1' else "",prem = 'selected' if product_num == '2' else "",dies = 'selected' if product_num =='3' else "",l = 'selected' if product_num =='4' else "",bd= 'selected' if product_num =='5' else "",s=suburbAndsurrounding)

	fuel_data_rows_string = "<html><body>" + fuel_data_rows_string + createfuelHTMLTABLE(FuelData)+"</body></html>"
    
	return HttpResponse(fuel_data_rows_string)

#def index(request):
	
#	return render(request,'fuel.html') 