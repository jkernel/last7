import sys
import requests
from selenium import webdriver
import time
##################################😎 PARE TA LINKS HEAD 2 HEAD #########################################

url_pr="https://www.statarea.com/predictions/date/today/starttime"
driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs',service_args=['--load-images=no','--disk-cache=true'])
driver.get(url_pr)
find_team1 = driver.find_elements_by_css_selector('div.match:nth-of-type(n+3) div.hostteam a.goals, div#\38 75207.match div.hostteam div.goals')

#ANOIGEI ARXEIO KAI TYPWNEI TO PROGRAMMA TWN AGWNVN 
fo=open('links-penalty.txt','w')
for element in find_team1:

   data=element.get_attribute("href")
   print(data,file=fo)
   
fo.close()
driver.quit()