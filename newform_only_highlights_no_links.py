import sys
import requests
from selenium import webdriver
import time
##################################😎 PARE TA LINKS HEAD 2 HEAD #########################################

#driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs')
#driver.get(url_pr)
#find_team1 = driver.find_elements_by_css_selector('div.hostteam div.name a')

#ANOIGEI ARXEIO KAI TYPWNEI TO PROGRAMMA TWN AGWNVN 
#fo=open('links.txt','w')
#for element in find_team1:

#   data=element.get_attribute("href")
#   print(data,file=fo)
   
#fo.close()
#driver.quit()

###############################😎 Split LINES IN .TXT FILE & opening WEBDRIVER at the 1st Url #####################################################


with open('links.txt','r') as fo:
   count=0
   for line in fo:
      count+=1
      
      url=line
      from selenium import webdriver
      driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs')
      driver.get(url)
      
 ##################################😎 HOME TEAM CONFIG ###################################################
      
      search_team1_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div#teamname.value')
      search_team1_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) span.name')
      search_team1_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.formastext')
      search_team1_avg_goals_scored = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(5) div.value')
      search_team1_avg_goals_conceded = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(6) div.value')
      
      team1_name = search_team1_name.text
      team1_country = search_team1_country.text          
      team1_last10 = search_team1_form.text   #😀 Kanei text ta last 10 formas
      team1_avg_goals_scored = search_team1_avg_goals_scored.text
      team1_avg_goals_conceded = search_team1_avg_goals_conceded.text

      
      
      #print(team1_last10)
      
      list(team1_last10)
      team1_last7=team1_last10[3:10]
      team1_last6=team1_last10[4:10]
      team1_last5=team1_last10[5:10]
      team1_7th=team1_last7[0]
      team1_6th=team1_last7[1]
      team1_5th=team1_last7[2]
      team1_4th=team1_last7[3]
      team1_3rd=team1_last7[4]
      team1_2nd=team1_last7[5]
      team1_1st=team1_last7[6]
   
    
      team1_wins_draws_losses=team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L')
      team1_sum_wins=team1_last6.count('W')
      team1_sum_draws=team1_last6.count('D')
      team1_sum_losses=team1_last6.count('L')
      team1_sum5_wins=team1_last5.count('W')
      team1_sum5_draws=team1_last5.count('D')
      team1_sum5_losses=team1_last5.count('L')
 
      team1_sum7_losses=team1_last7.count('L')    


      ##################################😎 AWAY TEAM CONFIG ###################################################
      
      search_team2_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div#teamname.value')
      search_team2_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) span.name')
      search_team2_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.formastext')
      
      
      
      team2_name = search_team2_name.text
      team1_country = search_team2_country.text     
      team2_last10 = search_team2_form.text   #😀 Kanei text ta last 10 formas
      
      
     
      
      
      #print(team2_last10)
      driver.quit()
      list(team2_last10)
      team2_last7=team2_last10[3:10]
      team2_last6=team2_last10[4:10]
      team2_last5=team2_last10[5:10]
      team2_7th=team2_last7[0]
      team2_6th=team2_last7[1]
      team2_5th=team2_last7[2]
      team2_4th=team2_last7[3]
      team2_3rd=team2_last7[4]
      team2_2nd=team2_last7[5]
      team2_1st=team2_last7[6]
      
    
      team2_wins_draws_losses=team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L')
      team2_sum_wins=team2_last6.count('W')
      team2_sum_draws=team2_last6.count('D')
      team2_sum_losses=team2_last6.count('L')
      team2_sum5_wins=team2_last5.count('W')
      team2_sum5_draws=team2_last5.count('D')
      team2_sum5_losses=team2_last5.count('L')
 
      team2_sum7_losses=team2_last7.count('L')    
      
      print("")
      print("Facts:")
     	
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==0 and team1_sum_draws==2 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
         print("{}-{} : Άσσος καρφωτό {}.".format(team1_name,team2_name))
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0):
         print("{}-{} : Άσσος καρφωτό {}.".format(team1_name,team2_name))
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
         print("{}-{} : Άσσος καρφωτό {}.".format(team1_name,team2_name))
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0):
         print( "{}-{} : Άσσος καρφωτό {}.".format(team1_name,team2_name) )        
   
      if (team1_sum_losses == team2_sum_losses+1 and 'L' in team1_7th):
        print("{}-{}. Η γηπεδούχος  έχει μια ήττα παραπάνω & ΉΤΤΑ στο 7ο!!! Νίκη για τους γηπεδούχους .".format(team1_name,team2_name))
    
      if (team2_sum7_losses ==0 and team1_sum7_losses==1):
        print("{}-{}. Η γηπεδούχος έχει έχει μία ήττα μόνο. Η φιλοξενούμενη 0 ήττες! Η ομάδα {} πρέπει να κερδίσει!".format(team1_name,team2_name,team1_name))
   
      if (team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
       print("{}-{}. Η γηπεδούχος έχει 1-1-4 και η φιλοξενούμενη 1-2-3!!! Φουλ του άσσου για την {}!!!".format(team1_name,team2_name,team1_name)) 

      if (team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and 'L' in team1_7th):
       print("---> {}-{}. Η γηπεδούχος έχει 1-1-4 & ήττα στο 7ο!!!!! Η ομάδα {} πάει για νίκη!!!".format(team1_name,team2_name,team1_name))
	
	
      if (team1_sum_wins==0 and team1_sum_draws==2 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3 ):
        print("---> {}-{}. Η γηπεδούχος έχει  0 νίκες & η φιλοξενούμενη 1-2-3!!! Νίκη για {}.".format(team1_name,team2_name,team1_name))	
	
      if (team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0 ):
        print("---> {}-{}. Η γηπεδούχος έχει 3-2-1 & η φιλοξενούμενη 0 ήττες!!!  {} will win." .format(team1_name,team2_name,team1_name))
	
      if (team1_sum_wins==4 and team1_sum_draws==0 and team1_sum_losses==2 and team2_sum_wins==4 and team2_sum_draws==0 and team2_sum_losses==2 ):
       print("---> {}-{}. Η γηπεδούχος έχει 4-0-2 & η φιλοξενούμενη 4-0-2!!! ΙΣΟΠΑΛΙΑ.".format(team1_name,team2_name))
       
      if (team1_sum_losses == team2_sum_losses and 'L' in team1_7th):
        print("{}-{}. Η γηπεδούχος έχει μια ήττα παραπάνω με την ΉΤΤΑ στο 7ο παιχνίδι!!! Νίκη ή ισοπαλία για τους γηπεδούχους.".format(team1_name,team2_name))
        
     
        
      
     


     
      print("###########*###################################*#######################################*##############################*##########################*############")    


