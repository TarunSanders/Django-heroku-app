#import requests
#r = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')
import feedparser
import operator #.add
from functools import reduce #reduce function
#from datetime import datetime
from pprint import pprint 
#
def get_fuel(suburbAndSurrounding,day): #gets list of dictionaries with fuel info and returns this data in own dictionary with imp info
	product_id = 1; #1: unleaded
	url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={prod}&Suburb={sub}&Day={D}' # product = ? query strings
	url = url.format(prod = str(product_id), sub = suburbAndSurrounding, D = day) #.format is not mutable function/method
	#print(url)
	data = feedparser.parse(url) #grabs RSS data from url and converts RSS to list of dictionaries format if not already
	
	dataImp = [ {'price': entry['price'], 
				'location': entry['location'],
				'brand':entry['brand'], 
				'date': entry['updated'],
				'address': entry['address'],
				'day': day}
			for entry in data['entries']
			]
	return(dataImp)

def by_price(x): # function handle for sort mutable method or sorted non-mutable function to sort prices in list of dictionaries x
	return x['price']

def createfuelHTMLTABLE(data): # creates fuel table with columns Price, Location, Brand, Address, date and highlights tomorrow's price
	blue ="#008080" #blue = "#008080"
	white = "#FFFFFF"
	header = '''
			<thead> 
				<tr> 
					<th> Price (Cents) </th> 
					<th> Location </th> 
					<th> Brand </th> 
					<th> Address </th> 
					<th> Date (Y-M-D) </th>
				</tr> 
			</thead>
			''' #heading format for html tables
	
	# loop creating body of table by iterating over each dictionary in list info grabbed f
		
	body = ''.join(
					'''
						<tbody>
							<tr bgcolor = {col}> 
								<td> {price} </td> 
								<td> {location} </td> 
								<td> {brand} </td> 
								<td> {address} </td> 
								<td> {date} </td> 
							</tr>
						</tbody>
			'''.format(**entry,col = blue if entry['day'] == 'tomorrow' else white) #unpacking dictionary entry in data
			for entry in data
	)
	argsT = [header, body]
	tableF = '''
			<table>
				{}
				{}
			</table>
			'''.format(*argsT)
	return tableF

def writeTable(tableDat,fileName,): #writing function for table
	with open(fileName,'w') as f:
		f.write(tableDat)	

def run(Suburb):
	
	Days = ['today','tomorrow']
	
	fuelInfo = reduce(operator.add, [get_fuel(Suburb,entry) for entry in Days]) # today and tomorrow's price using reduce and operator.add see packages
	
	fuelInfo.sort(key = by_price) #other option is to: fuelInfo = sorted(fuelInfo, key = by_price)
	#pprint(fuelInfo,indent=4)
	
	fuelTable = createfuelHTMLTABLE(fuelInfo)
	#writing full html string with fuel info to html file
	#htmlFilename = 'fuel in and near {}.html'.format(Suburb)
	htmlFilename = 'fuel.html'
	writeTable(fuelTable,htmlFilename)
	return fuelTable

print(__name__) #__name__ by default is main() from command prompt otherwise if importing it is name of file fuelwatch2.py
if __name__ == '__main__':
	suburb = input('Choose suburb: ')
	fuelTable = run(suburb) #executing main function nested with other defined functions
	#print(fuelTable)
#feedback from Robin Chew:
# use of **dic for unpacking arguments in dictionaries and *l for unpacking arguments in lists. e.g. minus(a,b) let d = {'a': 5, 'b':2} and l = [5, 2] then minus(**d) == minus(b=2,a=5) == minus(5,2) = minus(*l) etc etc
# create own dictionary
