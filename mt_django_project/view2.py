from django.http import HttpResponse
from mt_django_project.fuelwatch2 import sortedFuel, createfuelHTMLTABLE
from django.shortcuts import render
    
def index(request):

    product_num = request.GET.get('product')
	
    suburb = request.GET.get('suburb')
    
    surrounding =  request.GET.get('surrounding')
    if suburb == None:
        suburb = 'metro'
    if surrounding == None:
        FuelData = sortedFuel(suburb,product_num)
    else:
        FuelData = sortedFuel(suburb,product_num,surrounding)
    
    def ProdForm(i):
		
        prodOptionNames = ['Unleaded','Premium Unleaded','Diesel', 'LPG', 'Branded Diesel']
        
     ### old usage of .format ####
        #prodString = ''.join(f"""
        #                      <option value = {id} {select}> {prod} </option>
        #                    """.format(id = str(j+1), prod = entry, select = 'selected' if j+1 == i else '')
        #                    for j, entry in enumerate(prodOptionNamesName)
        #                   )
    
        ###using python3 f string feature
        prodString = ''.join(f"""
                              <option value = {str(j+1)} {'selected' if j+1 == i else ''}> {entry} </option>
                              """
                            for j, entry in enumerate(prodOptionNames))
        
		
        return prodString
	

    suburbForm = """
                    <b> Suburb (type 'metro' for all metro regions): </b> <input type="text" name="suburb" value ="{s}">
                    
                """.format(s=suburb)
	
    surroundingForm ="""
                      <b>Select to include surrounding suburbs</b>
                      <input type = "Checkbox" id = "surroundingInput" name = "surrounding" value = "yes" {}>
                    """.format('checked' if surrounding != None else '')
    
    
    num = int(product_num) if product_num != None else 0
	
    #fuel_data_rows_string = "<html><body>" + "<form autocomplete='on'>" + ProdForm(num) + suburbForm + "</form>"+createfuelHTMLTABLE(FuelData)+"</body></html>"
   
    return render(request, 'fuel.html',{'fuelTable': createfuelHTMLTABLE(FuelData),
                                        'options': ProdForm(num),
                                        'suburbs': suburbForm,
                                        'surrounding': surroundingForm,
                                        })

