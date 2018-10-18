import sys
import requests
from selenium import webdriver
import time
##################################😎 PARE TA LINKS HEAD 2 HEAD #########################################

url_pr="https://www.statarea.com/predictions"
driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs')
driver.get(url_pr)
find_team1 = driver.find_elements_by_css_selector('div.hostteam div.name a')

#ANOIGEI ARXEIO KAI TYPWNEI TO PROGRAMMA TWN AGWNVN 
fo=open('links.txt','w')
for element in find_team1:

   data=element.get_attribute("href")
   print(data,file=fo)
   
fo.close()
driver.quit()