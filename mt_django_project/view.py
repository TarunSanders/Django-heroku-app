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
	
	
	def ProdForm(i):
		
		prodName = ['Unleaded','Premium Unleaded','Diesel', 'LPG', 'Branded Diesel']
		
		
		prodString = ''.join("""
								<option value = {id}{select}> {prod} </option>
							""".format(id = str(j), prod = entry, select = 'selected' if j == i else '')
							for j, entry in enumerate(prodName)
							)
		prodString = '<select name = "product" autocomplete="on">' + prodString + '</select>'
		return prodString
	

	suburbForm = """
				Suburb and surrounding (type 'metro' for all metro regions): <input type="text" name="suburb" value ="{s}">
  			    <button type="submit"> Enter </button> 
				 """.format(s=suburbAndsurrounding)
	
	
	prod = int(product_num) if product_num != None else 0
	
	
	fuel_data_rows_string = "<html><body>" + "<form autocomplete='on'>" + ProdForm(prod) + suburbForm + "</form>"+createfuelHTMLTABLE(FuelData)+"</body></html>"
    
	return HttpResponse(fuel_data_rows_string)

