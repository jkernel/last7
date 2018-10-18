import sys
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


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
      try:
	      search_team1_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div#teamname.value')
	      search_team1_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) span.name')
	      search_team1_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.formastext')
	      search_team1_avg_goals_scored = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(5) div.value')
	      search_team1_avg_goals_conceded = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(6) div.value')
	      search_team1_world_rank= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.datarow:nth-of-type(5) div.value')
	      search_team1_chance_score= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(7) div.value')
	      search_team1_chance_concede= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(8) div.value')
	      
      except NoSuchElementException:
      	print("Element not found")
      team1_name = search_team1_name.text
      team1_country = search_team1_country.text          
      team1_last10 = search_team1_form.text   #😀 Kanei text ta last 10 formas
      team1_avg_goals_scored = search_team1_avg_goals_scored.text
      team1_avg_goals_conceded = search_team1_avg_goals_conceded.text
      team1_int_avg_scored= float(team1_avg_goals_scored)
      team1_int_avg_conceded= float(team1_avg_goals_conceded)
      team1_world_rank= search_team1_world_rank.text
      team1_chance_to_score= search_team1_chance_score.text
      team1_nosymbol_chance_to_score= team1_chance_to_score.strip('%')  #afairesh symbolou %
      team1_int_chance_to_score=int(team1_nosymbol_chance_to_score)
      team1_chance_to_concede= search_team1_chance_concede.text
      team1_nosymbol_chance_to_concede=team1_chance_to_concede.strip('%')
      team1_int_chance_to_concede=int(team1_nosymbol_chance_to_concede)  
      
      
      print("")
      print("Home Team: ",team1_name)
      try:
	      team1_int_world_rank= int(team1_world_rank)
	      print("World Rank: ",team1_int_world_rank)
	      
      except ValueError:
      	print("Δεν έχει World Rank")
      	
      
      print("---> AVG goals scored: ",team1_avg_goals_scored)
      print("---> AVG goals conceded: ",team1_avg_goals_conceded)
      print("Chance to score: ",team1_int_chance_to_score,"%")
      print("Chance to concede: ",team1_int_chance_to_concede,"%")
     
      
      
      #print(team1_last10)
      try:
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
      except:
      	pass
      #print(team1_name)
      print(" 7=",team1_7th,"6=",team1_6th,"5=",team1_5th,"4=",team1_4th,"3=",team1_3rd,"2=",team1_2nd,"1=",team1_1st,"--->")
      print(" Φόρμα7:",team1_last7.count('W'),"-",team1_last7.count('D'),"-",team1_last7.count('L'))
      print(" Φόρμα6:",team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L'))
      print(" Φόρμα5:",team1_last5.count('W'),"-",team1_last5.count('D'),"-",team1_last5.count('L'))
    
      team1_wins_draws_losses=team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L')
      team1_sum_wins=team1_last6.count('W')
      team1_sum_draws=team1_last6.count('D')
      team1_sum_losses=team1_last6.count('L')
      team1_sum5_wins=team1_last5.count('W')
      team1_sum5_draws=team1_last5.count('D')
      team1_sum5_losses=team1_last5.count('L')
 
      team1_sum7_losses=team1_last7.count('L')    
      print(" Συνολικές ήττες",team1_sum7_losses)
      
      print("")
      print("VS")
      print("")

      ##################################😎 AWAY TEAM CONFIG ###################################################
      try:
	      search_team2_name = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div#teamname.value')
	      search_team2_country = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) span.name')
	      search_team2_form = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.formastext')
	      search_team2_avg_goals_scored = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(5) div.value')
	      search_team2_avg_goals_conceded = driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(6) div.value')
	      search_team2_world_rank= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.datarow:nth-of-type(5) div.value')
	      search_team2_chance_score= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(7) div.value')
	      search_team2_chance_concede= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(8) div.value')
	      
      except NoSuchElementException:
         print("Element of Away Team not found")   
      team2_name = search_team2_name.text
      team1_country = search_team2_country.text     
      team2_last10 = search_team2_form.text   #😀 Kanei text ta last 10 formas
      team2_avg_goals_scored = search_team2_avg_goals_scored.text
      team2_avg_goals_conceded = search_team2_avg_goals_conceded.text
      team2_int_avg_scored= float(team2_avg_goals_scored)
      team2_int_avg_conceded= float(team2_avg_goals_conceded)
      team2_world_rank= search_team2_world_rank.text      
      team2_chance_to_score= search_team2_chance_score.text
      team2_nosymbol_chance_to_score= team2_chance_to_score.strip('%')
      team2_int_chance_to_score=int(team2_nosymbol_chance_to_score)
      team2_chance_to_concede= search_team2_chance_concede.text
      team2_nosymbol_chance_to_concede=team2_chance_to_concede.strip('%')
      team2_int_chance_to_concede=int(team2_nosymbol_chance_to_concede)

      
      print("")
      print("Away Team: ",team2_name)
      try:
	      team2_int_world_rank= int(team2_world_rank)
	      print("World Rank: ",team2_int_world_rank)
      except ValueError:
      	print("Δεν έχει World Rank")
      
      print(" ---> AVG goals scored: ",team2_avg_goals_scored,"goals per match")
      print(" ---> AVG goals conceded: ",team2_avg_goals_conceded,"goals per match")
      print("Chance to score: ",team2_int_chance_to_score,"%")
      print("Chance to concede: ",team2_int_chance_to_concede,"%")
      
      
      #print(team2_last10)
      driver.quit()
      try:
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
      except:
      	pass
      #print(team1_name)
      print(" 7=",team2_7th,"6=",team2_6th,"5=",team2_5th,"4=",team2_4th,"3=",team2_3rd,"2=",team2_2nd,"1=",team2_1st)
      print(" Φόρμα7:",team2_last7.count('W'),"-",team2_last7.count('D'),"-",team2_last7.count('L'))
      print(" Φόρμα6:",team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L'))
      print(" Φόρμα5:",team2_last5.count('W'),"-",team2_last5.count('D'),"-",team2_last5.count('L'))
    
      team2_wins_draws_losses=team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L')
      team2_sum_wins=team2_last6.count('W')
      team2_sum_draws=team2_last6.count('D')
      team2_sum_losses=team2_last6.count('L')
      team2_sum5_wins=team2_last5.count('W')
      team2_sum5_draws=team2_last5.count('D')
      team2_sum5_losses=team2_last5.count('L')
 
      team2_sum7_losses=team2_last7.count('L')    
      print(" Συνολικές ήττες",team2_sum7_losses)
      print("")
      print("Facts:")
      if 'L' in team1_7th:
      	print("-->Home Team--> ΉΤΤΑ στο 7ο!")
      	
      if 'L' in team2_7th:
      	print("-->Away Team--> ΉΤΤΑ στο 7ο!")	
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==0 and team1_sum_draws==2 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
         highlight1_match="Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name)
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0):
         highlight2_match="Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name)
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
         highlight3_match= ("Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0):
         highlight4_match= ("Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name))         
      
      if (team1_sum7_losses == team2_sum7_losses+1):
        print("---> Η γηπεδούχος {} έχει μια ήττα παραπάνω! Πάει για νίκη!".format(team1_name))
        
    
      if (team1_sum7_losses == team2_sum7_losses):
        print("---> Ισάριθμες ήττες ({})! Μυρίζει Ισοπαλία!".format(team1_sum7_losses))   
    
      if (team2_sum7_losses == (team1_sum7_losses+1)):
        print("---> Η φιλοξενούμενη {} έχει μια ήττα παραπάνω! Πάνε για θετικό αποτέλεσμα!".format(team2_name))    
   
      if (team1_sum_losses == team2_sum_losses+1 and 'L' in team1_7th):
        print("---> Η γηπεδούχος έχει έχει μια ήττα παραπάνω & ΉΤΤΑ στο 7ο!!! Νίκη για {}.".format(team1_name))
    
      if (team2_sum7_losses ==0 and team1_sum7_losses==1):
        print("---> Η γηπεδούχος έχει έχει μία ήττα μόνο. Η φιλοξενούμενη 0 ήττες! Η ομάδα {} πρέπει να κερδίσει!".format(team1_name))
    
      if (team1_sum7_losses ==0 and team2_sum7_losses==1):
        print("---> Η γηπεδούχος έχει 0 ήττες. Η φιλοξενούμενη 1 ήττα! Δύσκολο ματς για τους γηπεδούχους.".format(team2_name))      
   
      if (team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
        print("---> Η γηπεδούχος έχει 1-1-4 και η φιλοξενούμενη 1-2-3!!! Φουλ του άσσου για την {}!!!".format(team1_name)) 
	 

      if (team1_sum_wins==1 and team1_sum_draws==1 and team1_sum_losses==4 and 'L' in team1_7th):
        print("---> Η γηπεδούχος έχει 1-1-4 & ήττα στο 7ο!!!!! Η ομάδα {} πάει για νίκη!!!".format(team1_name))
	
      if (team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1):
        print("---> Η γηπεδούχος έχει 3-2-1 !!!  Αυξημένες πιθανότητες νίκης για την ομάδα {}." .format(team1_name)) 
      if (team1_sum_wins==3 and team1_sum_draws==1 and team1_sum_losses==2):
        print("---> Η γηπεδούχος έχει 3-2-1 !!!  Αυξημένες πιθανότητες νίκης για την ομάδα {}." .format(team1_name)) 		
	 
      if (team2_sum_wins==4 and team2_sum_draws==1 and team2_sum_losses==1):
        print("---> Η φιλοξενούμενη {} έχει 4-1-1 !!!   Θ ." .format(team2_name))
	
      if (team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3):
        print("---> Η φιλοξενούμενη έχει 1-2-3!!! Η ομάδα {} θα τα βρεί σκούρα." .format(team2_name))
	
      if (team1_sum_wins==0 or team1_sum_draws==0 or team1_sum_losses==0):
        print("---> Η γηπεδούχος έχει 0 WDL!  Ίσως το 0 γίνει 1 για την ομάδα {}." .format(team1_name))
	
      if (team2_sum_wins==0 or team2_sum_draws==0 or team2_sum_losses==0):
        print("---> Η φιλοξενούμενη έχει 0 WDL!  Ίσως το 0 γίνει 1 για την ομάδα {}." .format(team2_name))
	
      if (team1_sum_wins==0 and team1_sum_draws==2 and team1_sum_losses==4 and team2_sum_wins==1 and team2_sum_draws==2 and team2_sum_losses==3 ):
        print("---> Η γηπεδούχος έχει  0 νίκες & η φιλοξενούμενη 1-2-3!!! Νίκη για {}.".format(team1_name))	
	
      if (team1_sum_wins==3 and team1_sum_draws==2 and team1_sum_losses==1 and team2_sum_wins==4 and team2_sum_draws==2 and team2_sum_losses==0 ):
        print("---> Η γηπεδούχος έχει 3-2-1 & η φιλοξενούμενη 0 ήττες!!!  {} will win." .format(team1_name))	
	
      if (team1_sum_wins==4 and team1_sum_draws==0 and team1_sum_losses==2 and team2_sum_wins==4 and team2_sum_draws==0 and team2_sum_losses==2 ):
        print("---> Η γηπεδούχος έχει 4-0-2 & η φιλοξενούμενη 4-0-2!!! ΙΣΟΠΑΛΙΑ.")
        
      if (team1_sum5_wins==2 and team1_sum5_draws==2 and team1_sum5_losses==1):
        print("---> Η φόρμα5 δείχνει Νίκη ή Ισοπαλία για την ομάδα {}.".format(team1_name))
        
      if (team1_sum5_wins==1 and team1_sum5_draws==2 and team1_sum5_losses==2):
        print("---> Η φόρμα5 δείχνει Ισοπαλία ή Ήττα για την ομάδα {}.".format(team1_name))
          
      if (team1_sum5_wins==2 and team1_sum5_draws==1 and team1_sum5_losses==2):
    	  print("---> Η φόρμα5 δείχνει Νίκη ή Ήττα για την ομάδα {}.".format(team1_name))
      if (team2_sum5_wins==2 and team2_sum5_draws==2 and team2_sum5_losses==1):
        print("---> Η φόρμα5 δείχνει Νίκη ή Ισοπαλία για την ομάδα {}.".format(team2_name))
        
      if (team2_sum5_wins==1 and team2_sum5_draws==2 and team2_sum5_losses==2):
        print("---> Η φόρμα5 δείχνει Ισοπαλία ή Ήττα για την ομάδα {}.".format(team2_name))
          
      if (team2_sum5_wins==2 and team2_sum5_draws==1 and team2_sum5_losses==2):
    	  print("---> Η φόρμα5 δείχνει Νίκη ή Ήττα για την ομάδα {}.".format(team2_name))
    
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.5 and team1_int_avg_conceded<0.5 and team2_int_avg_conceded>2):
      	print("{}-{}. Η γηπεδούχος σκοράρει κατα ριππάς και δέχεται γκολ με το σταγονόμετρο!!! Η φιλοξενούμενη δε βάζει γκολ και τρώει πάνω απο 2 σε κάθε ματς!!!!!".format(team1_name,team2_name)) 
        
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.6 and team1_int_avg_conceded<0.7 and team2_int_avg_conceded>1.7):
      	print("{}-{}. Η γηπεδούχος σκοράρει πανω απο 2 γκολ σε κάθε ματς και δέχεται γκολ κάτω από 0.7. Η φιλοξενούμενη βάζει γκολ <0.7 και τρώει πάνω απο 2 σε κάθε ματς".format(team1_name,team2_name))   
      
      #if (team1_int_chance_to_score>80 and team2_int_chance_to_score<30 and team1_int_chance_to_concede<30 and team1_int_chance_to_concede>70):
      	#print("{}-{}. Η γηπεδούχος έχει πάνω απο 80% να σκοράρει στο προσεχές ματς και λιγότερο απο 30% να δεχτεί. Η φιλοξενούμενη δε σκοράρει και δέχεται με ευκολία γκολ. Η γηπεδούχοι θα κερδίσουν!!!".format(team1_name,team2_name))
      
      if (team1_int_chance_to_score>75 and team2_int_chance_to_score<35 and team1_int_chance_to_concede<35 and team1_int_chance_to_concede>70):
      	print("{}-{}. Η γηπεδούχος έχει πάνω απο 75% να σκοράρει στο προσεχές ματς και λιγότερο απο 35% να δεχτεί. Η φιλοξενούμενη δε σκοράρει και δέχεται με ευκολία γκολ. Η γηπεδούχοι θα κερδίσουν!!!".format(team1_name,team2_name))      
       
      print("")
      print("")
      #print("Τελευταίο ματς:",teams_history)
      print("###########*###################################*#######################################*##############################*##########################*############")    


