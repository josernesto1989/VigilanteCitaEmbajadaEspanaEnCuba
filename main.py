from gmail import MailTo

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import winsound

#url of the page we want to scrape
url1 = "http://www.exteriores.gob.es/Consulados/LAHABANA/es/Tramites/Visados/Paginas/Visado-de-estudios-o-investigaci%c3%b3n,-movilidad-de-alumnos,-pr%c3%a1cticas-no-laborales-o-servicios-de-voluntariado-de-duraci%c3%b3n-su.aspx"

driver = webdriver.Chrome('./chromedriver') 
f = open("Resultado.txt", "w")
f.close()

#http://www.exteriores.gob.es/Consulados/LAHABANA/es/Tramites/Visados/Paginas/Visado-de-estudios-o-investigaci%c3%b3n,-movilidad-de-alumnos,-pr%c3%a1cticas-no-laborales-o-servicios-de-voluntariado-de-duraci%c3%b3n-su.aspx
#idCaptchaButton get href

for x  in range(90):
    print("entrando a ciclo")
    driver.get(url1)
    print("leyndo url y esperando...")
    
    # # this is just to ensure that the page is loaded
    time.sleep(5)   
    print("termina la espera")
    
    html = driver.page_source    
    print("obtenido html")
    # # # this renders the JS code and stores all
    # # # of the information in static HTML code.    
    # # # Now, we could simply apply bs4 to html variable
    soup = BeautifulSoup(html, "html.parser")
    
    attr = soup.find('a', {'class':"natural"})

    link = driver.find_element_by_link_text('Reservar cita de Visado')
    
    if(link is not None):
        
        print("encontrado")
        link.click()
        print("clickeado")
        time.sleep(5) 
        driver.switch_to.window(driver.window_handles[1])

        driver.find_element_by_css_selector('#idCaptchaButton').click()
        print("clickead 2do boton")
        time.sleep(300)
        ##idDivNotAvailableSlotsTextTop
        # driver.
        # driver.findE
        attr = driver.find_element_by_id('idDivNotAvailableSlotsTextTop')
        print("******************************************************************************************************************************************")
        print(attr)
#No hay horas disponibles. Inténtelo de nuevo mañana.
        # listAttr= ((str)(attr)).split("\"")
        # if(listAttr.__len__()>3):
        #     url2= listAttr[3]
        #     print("entrando a url:")
        #     print(url2)
        #     driver.get(url2)
        #     print("cargada url2")
        #     time.sleep(100)
    else:
        print("NADA")
   # f = open("Resultado.txt", "a")
   # #print('mmmmmm')
   # if(viajes is not None):
   #     f.write(dateStr+": Hay viaje *****;)\n")
   # else:
   #     f.write(dateStr+": No hay viaje :(\n")
   #     isCaptcha = soup.findAll('h1')
   #     #print(isCaptcha)
   #     for x in isCaptcha:
   #         if(x.text == "Disculpe los Inconvenientes"):
   #             frequency = 2500  # Set Frequency To 2500 Hertz
   #             duration = 2000  # Set Duration To 1000 ms == 1 second
   #             winsound.Beep(frequency, duration)
   #             time.sleep(30)
   #     
   #     #<h1>Disculpe los Inconvenientes</h1>
#
    f.close()
    
driver.close() # closing the webdriver
