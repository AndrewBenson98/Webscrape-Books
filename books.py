from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#Open a file to save the data to 
filename = "books.csv"
f = open(filename,"w")

#Set the headers and write to file
headers = "title,price,stock,rating\n"
f.write(headers)


for i in range(1,51):
	my_url = 'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'

	#Opening connection, grabbing page
	uClient = uReq(my_url)
	page_html=uClient.read()
	uClient.close()

	#html parsing
	page_soup = soup(page_html,"html.parser")

	#List of all blocks of html in div that have the class 'item-container'
	containers  = page_soup.findAll("article",{"class":"product_pod"})



	#For every container with the Product_pod class
	for container in containers:
		#Get the title
		title =container.h3.a["title"]
		
		#Get the product price
		price_container = container.findAll("div",{"class":"product_price"})
		price = price_container[0].find('p').getText()
		
		#Get stock
		stock_container = price_container[0].findAll("p",{"class":"instock availability"})
		stock = stock_container[0].getText().strip()

		#Get the rating for the book
		rating_word = container.find('p')["class"][1]
		if(rating_word == "One"):
			rating="1"
		elif(rating_word == "Two"):
			rating="2"
		elif(rating_word == "Three"):
			rating="3"
		elif(rating_word == "Four"):
			rating="4"
		elif(rating_word == "Five"):
			rating="5"
		else: rating = "NA"


		#Write data to the file
		f.write(title.replace(",","|")+","+price +","+stock+","+rating+"\n")
	
f.close()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
