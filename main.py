from gmail import MailTo

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import winsound

#url of the page we want to scrape
url1 = "https://shopping.copaair.com/?roundtrip=false&adults=1&children=0&infants=0&date1="
now = datetime.datetime.now()
#url2 = "&date2=null&promocode=&area1=GUA&area2=GEO&advanced_air_search=false&flexible_dates_v2=false"  
url2 = "&date2=null&promocode=&area1=HAV&area2=GEO&advanced_air_search=false&flexible_dates_v2=false"  

driver = webdriver.Chrome('./chromedriver') 
f = open("Resultado.txt", "w")
f.close()

for x  in range(90):
    currentDate = now + datetime.timedelta(days=0+x)    
    dateStr = str(currentDate.year)+'-'+("", "0")[currentDate.month<10]+str(currentDate.month)+'-'+("", "0")[currentDate.day<10]+str(currentDate.day)
    driver.get(url1+dateStr+url2)
    # # this is just to ensure that the page is loaded
    time.sleep(3)     
    html = driver.page_source    

    # # # this renders the JS code and stores all
    # # # of the information in static HTML code.    
    # # # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    viajes = soup.find('div', {'role':"listitem"})
    f = open("Resultado.txt", "a")
    #print('mmmmmm')
    if(viajes is not None):
        f.write(dateStr+": Hay viaje *****;)\n")
    else:
        f.write(dateStr+": No hay viaje :(\n")
        isCaptcha = soup.findAll('h1')
        #print(isCaptcha)
        for x in isCaptcha:
            if(x.text == "Disculpe los Inconvenientes"):
                frequency = 2500  # Set Frequency To 2500 Hertz
                duration = 2000  # Set Duration To 1000 ms == 1 second
                winsound.Beep(frequency, duration)
                time.sleep(30)
        
        #<h1>Disculpe los Inconvenientes</h1>

    f.close()
    
driver.close() # closing the webdriver
