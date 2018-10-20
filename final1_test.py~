import sys
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
##################################😎 PARE TA LINKS HEAD 2 HEAD #########################################

url_pr="https://www.statarea.com/predictions/date/today/starttime"
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

###############################😎 Split LINES IN .TXT FILE & opening WEBDRIVER at the 1st Url #####################################################


with open('links.txt','r') as fo:
   count=0
   for line in fo:
      count+=1
      
      url=line
      from selenium import webdriver
      driver=webdriver.PhantomJS('/home/jkernel/Desktop/python books/phantomjs/bin/phantomjs')
      driver.get(url)
      time.sleep(3)
      
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
	      search_team1_over_1_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(8) div.barrow:nth-of-type(1) div.bar')
	      search_team1_over_2_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(10) div.barrow:nth-of-type(1) div.bar')
	      search_team1_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
	      search_team1_last10_cleansheet= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(9) div.value')
	      search_team1_last10_failtoscore= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.factitem:nth-of-type(10) div.value')
	      
	      search_game_datetime= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(1) div.starttime')


	      
	      
	      
      except NoSuchElementException:
      	print("Element of Home Team not found")
      	
      game_datetime=search_game_datetime.text
      	
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
      team1_over_1_5_mats= search_team1_over_1_5_mats.text
      team1_over_1_5_mats_nosymbol= team1_over_1_5_mats.strip('%')  #afairesh symbolou %
      team1_over_1_5_int= int(team1_over_1_5_mats_nosymbol)
      team1_over_2_5_mats= search_team1_over_2_5_mats.text
      team1_over_2_5_mats_nosymbol= team1_over_2_5_mats.strip('%')
      team1_over_2_5_int= int(team1_over_2_5_mats_nosymbol)
      team1_btts= search_team1_btts.text
      team1_btts_nosymbol= team1_btts.strip('%')
      team1_btts_int= int(team1_btts_nosymbol)
      team1_last10_cleansheet= search_team1_last10_cleansheet.text
      team1_last10_cleansheet_int= int(team1_last10_cleansheet)
      team1_last10_failtoscore= search_team1_last10_failtoscore.text
      team1_last10_failtoscore_int= int(team1_last10_failtoscore)
      
      
      
      
      try:
      	search_history_team1_wins= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(3) div.value')
      	search_history_draws= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(4) div.value')
      	search_history_team2_wins= driver.find_element_by_css_selector('div.facts div.datarow:nth-of-type(5) div.value')
      	history_team1_wins= search_history_team1_wins.text
      	history_draws= search_history_draws.text
      	history_team2_wins= search_history_team2_wins.text
      except NoSuchElementException:
      	print("Element of History not found")  
      
      
      print("Χώρα: ",team1_country)
      print("Έναρξη: ",game_datetime)
      print("")
      print("Home Team: ",team1_name)
      
      try:
	      team1_int_world_rank= int(team1_world_rank)
	      print("World Rank: ",team1_int_world_rank)	      
      except ValueError:
      	print("Δεν έχουν World Rank")
      	
      
      print("Μ.Ο γκολ που σκοράρουν: ",team1_avg_goals_scored)
      print("Μ.Ο γκολ που δέχεται: ",team1_avg_goals_conceded)
      print("Πιθανότητα να βάλει γκολ: ",team1_int_chance_to_score,"%")
      print("Πιθανότητα να δεχτούν γκολ: ",team1_int_chance_to_concede,"%")
      print("Ποσοστό Over 1,5: ",team1_over_1_5_int,"%")
      print("Ποσοστό Over 2,5: ",team1_over_2_5_int,"%")
      print("Ποσοστό BTTS: ",team1_btts_int,"%")
      print("Clean Sheet στα last10: ",team1_last10_cleansheet_int)
      print("Fail to Score στα last10: ",team1_last10_failtoscore_int)
     
      
      
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
	      print(team1_7th,team1_6th,team1_5th,team1_4th,team1_3rd,team1_2nd,team1_1st)
      except:
      	pass
      #print(team1_name)
      
      print(" Φ7:",team1_last7.count('W'),"-",team1_last7.count('D'),"-",team1_last7.count('L'))
      print(" Φ6:",team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L'))
      print(" Φ5:",team1_last5.count('W'),"-",team1_last5.count('D'),"-",team1_last5.count('L'))
    
      team1_wins_draws_losses=team1_last6.count('W'),"-",team1_last6.count('D'),"-",team1_last6.count('L')
      team1_sum6_wins=team1_last6.count('W')
      team1_sum6_draws=team1_last6.count('D')
      team1_sum6_losses=team1_last6.count('L')
      team1_sum5_wins=team1_last5.count('W')
      team1_sum5_draws=team1_last5.count('D')
      team1_sum5_losses=team1_last5.count('L')
 
      team1_sum7_wins=team1_last7.count('W')
      team1_sum7_draws=team1_last7.count('D')      
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
	      search_team2_over_1_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(8) div.barrow:nth-of-type(1) div.bar')
	      search_team2_over_2_5_mats= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(10) div.barrow:nth-of-type(1) div.bar')
	      search_team2_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
	      search_team2_btts= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.barchart:nth-of-type(17) div.barrow:nth-of-type(1) div.bar')
	      search_team2_last10_cleansheet= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(9) div.value')
	      search_team2_last10_failtoscore= driver.find_element_by_css_selector('div.halfcontainer:nth-of-type(2) div.factitem:nth-of-type(10) div.value')
	      
      except NoSuchElementException:
         print("Element of Away Team not found")   
      team2_name = search_team2_name.text
      team2_country = search_team2_country.text     
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
      team2_over_1_5_mats= search_team2_over_1_5_mats.text
      team2_over_1_5_mats_nosymbol= team2_over_1_5_mats.strip('%')  #afairesh symbolou %
      team2_over_1_5_int= int(team2_over_1_5_mats_nosymbol)
      team2_over_2_5_mats= search_team2_over_2_5_mats.text
      team2_over_2_5_mats_nosymbol= team2_over_2_5_mats.strip('%')
      team2_over_2_5_int= int(team2_over_2_5_mats_nosymbol)
      team2_btts= search_team2_btts.text
      team2_btts_nosymbol= team2_btts.strip('%')
      team2_btts_int= int(team2_btts_nosymbol)
      team2_last10_cleansheet= search_team2_last10_cleansheet.text
      team2_last10_cleansheet_int= int(team2_last10_cleansheet)
      team2_last10_failtoscore= search_team2_last10_failtoscore.text
      team2_last10_failtoscore_int= int(team2_last10_failtoscore)
        
      
      print("Χώρα: ",team2_country)
      print("Away Team: ",team2_name)
      
      try:
	      team2_int_world_rank= int(team2_world_rank)
	      print("World Rank: ",team2_int_world_rank)
      except ValueError:
      	print("Δεν έχουν World Rank")
      
      print("Μ.Ο γκολ που σκοράρουν: ",team2_avg_goals_scored)
      print("Μ.Ο γκολ που δέχεται: ",team2_avg_goals_conceded)
      print("Πιθανότητα να βάλει γκολ: ",team2_int_chance_to_score,"%")
      print("Πιθανότητα να δεχτούν γκολ: ",team2_int_chance_to_concede,"%")
      try:
	      team2_int_world_rank= int(team2_world_rank)
	      print("Ποσοστό Over 1,5: ",team2_over_1_5_int,"%")
      except ValueError:
      	print("Δεν έχουν World Rank")
      
      print("Ποσοστό Over 2,5: ",team2_over_2_5_int,"%")
      print("Ποσοστό BTTS: ",team2_btts_int,"%")
      print("Clean Sheet στα last10: ",team2_last10_cleansheet_int)
      print("Fail to Score στα last10: ",team2_last10_failtoscore_int)
      
      
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
      print(team2_7th,team2_6th,team2_5th,team2_4th,team2_3rd,team2_2nd,team2_1st)
      print(" Φ7:",team2_last7.count('W'),"-",team2_last7.count('D'),"-",team2_last7.count('L'))
      print(" Φ6:",team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L'))
      print(" Φ5:",team2_last5.count('W'),"-",team2_last5.count('D'),"-",team2_last5.count('L'))
    
      team2_wins_draws_losses=team2_last6.count('W'),"-",team2_last6.count('D'),"-",team2_last6.count('L')
      team2_sum6_wins=team2_last6.count('W')
      team2_sum6_draws=team2_last6.count('D')
      team2_sum6_losses=team2_last6.count('L')
      team2_sum5_wins=team2_last5.count('W')
      team2_sum5_draws=team2_last5.count('D')
      team2_sum5_losses=team2_last5.count('L')
 
      team2_sum7_wins=team2_last7.count('W')
      team2_sum7_draws=team2_last7.count('D')
      team2_sum7_losses=team2_last7.count('L')    
      print(" Συνολικές ήττες",team2_sum7_losses)
      print("")
      print("Facts:")
      
      if 'L' in team1_7th:
      	print("-->Home Team--> ΉΤΤΑ στο 7ο!")
      	
      if 'L' in team2_7th:
      	print("-->Away Team--> ΉΤΤΑ στο 7ο!")
      try:
      	print("Προϊστορία: Οι γηπεδούχοι μετρούν συνολικά {} νίκες ενώ οι φιλοξενούμενοι {}. Οι ισοπαλίες ήταν {}.".format(history_team1_wins,history_team2_wins,history_draws))
      except NameError:
      	print ("Δεν έχουν Προϊστορία")
      	
      	
      try:	
	      if (team1_int_world_rank > team2_int_world_rank+400):
	        print("---> Οι γηπεδούχοι {} έχουν βαρύτερη φανέλα λόγω World Rank !".format(team1_name))
	      if (team2_int_world_rank > team1_int_world_rank+400):
	        print("---> Οι φιλοξενούμενοι {} έχουν βαρύτερη φανέλα λόγω World Rank !".format(team2_name))  
      except NameError:
      	print("Κάποια ομάδα δεν έχουν World Rank.")
        		
      if (team1_sum6_wins==0 and team1_sum6_draws==2 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
         print("Κριτήριο 024+123!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0):
         print("Κριτήριο 321+420!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         
      if (team1_sum6_wins==2 and team1_sum6_draws==1 and team1_sum6_losses==3 and 'L' in team1_1st and 'L' in team1_2nd and 'L' in team1_3rd):
      	print("Οι γηπεδούχοι έχουν 213 με 3 συνεχόμενες ήττες. Πάνε για θετικό αποτέλεσμα.")
      
      if (team1_sum6_wins==1 and team1_sum6_draws==2 and team1_sum6_losses==3 and 'L' in team1_1st and 'L' in team1_2nd and 'L' in team1_3rd):
         highlight3_match= "Οι γηπεδούχοι έχουν 123 με 3 συνεχόμενες ήττες. Πάνε για θετικό αποτέλεσμα."
      
      if (team1_sum6_wins==team2_sum6_wins-1 and team1_sum6_draws==team2_sum6_draws and team1_sum6_losses== team2_sum6_losses+1 and 'L' in team1_7th):
         print("Οι γηπεδούχοι με νίκη ισορροπούν τη φόρμα πλήρως{}.")
      
      if (team1_sum6_wins==team2_sum6_wins-1 and team1_sum6_draws==team2_sum6_draws and team1_sum6_losses== team2_sum6_losses+1 and 'L' in team1_7th):
         print("Οι γηπεδούχοι με νίκη ισορροπούν τη φόρμα πλήρως{}.")
      
      if (team1_sum6_wins==team2_sum6_wins and team1_sum6_draws==team2_sum6_draws and team1_sum7_losses== team2_sum7_losses+1 ):
         print("Οι γηπεδούχοι με νίκη ισορροπούν τη φόρμα πλήρως{}.")
      
      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
         print("Κριτήριο 114+123!!!: Νίκη της γηπεδούχου ομάδας {}.".format(team1_name))
         
      if (team1_sum7_losses == team2_sum7_losses+1 and 'L' in team1_7th and 'D' in team2_7th and team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0):
         print("Δεδομένη η νίκη της γηπεδούχου ομάδας {}.".format(team1_name))         
      
      if (team1_sum7_losses == team2_sum7_losses+1):
        print("---> Οι γηπεδούχοι {} έχουν μια ήττα παραπάνω! Πάει για νίκη!".format(team1_name))
        
    
      if (team1_sum7_losses == team2_sum7_losses):
        print("---> Ισάριθμες ήττες ({})! Μυρίζει Ισοπαλία!".format(team1_sum7_losses))   
    
      if (team2_sum7_losses == (team1_sum7_losses+1)):
        print("---> Οι φιλοξενούμενοι {} έχουν μια ήττα παραπάνω! Πάνε για θετικό αποτέλεσμα!".format(team2_name))    
   
      if (team1_sum6_losses == team2_sum6_losses+1 and 'L' in team1_7th):
        print("---> Οι γηπεδούχοι έχουν έχουν μια ήττα παραπάνω & ΉΤΤΑ στο 7ο!!! Νίκη για {}.".format(team1_name))
    
      if (team2_sum7_losses ==0 and team1_sum7_losses==1):
        print("---> Οι γηπεδούχοι έχουν έχουν μία ήττα μόνο. Οι φιλοξενούμενοι 0 ήττες! Η ομάδα {} πρέπει να κερδίσει!".format(team1_name))
    
      
      
      if (team1_sum7_losses ==0 and team2_sum7_losses==1):
        print("---> Οι γηπεδούχοι έχουν 0 ήττες. Οι φιλοξενούμενοι 1 ήττα! Δύσκολο ματς για τους γηπεδούχους.".format(team2_name))      
   
      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
        print("---> Οι γηπεδούχοι έχουν 1-1-4 και οι φιλοξενούμενοι 1-2-3!!! Φουλ του άσσου για {}!!!".format(team1_name)) 
	 

      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and 'L' in team1_7th and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3 and 'D' in team2_7th ):
        print("---> Οι γηπεδούχοι έχουν 1-1-4 & ήττα στο 7ο!!!!! Η ομάδα {} πάει για νίκη!!!".format(team1_name))
      
      if (team1_sum6_wins==1 and team1_sum6_draws==1 and team1_sum6_losses==4 and 'L' in team1_7th):
        print("---> Οι γηπεδούχοι έχουν 1-1-4 & ήττα στο 7ο!!!!! Η ομάδα {} πάει για νίκη!!!".format(team1_name))
	
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1):
        print("---> Οι γηπεδούχοι έχουν 3-2-1 !!!  Αυξημένες πιθανότητες νίκης για την ομάδα {}." .format(team1_name)) 
      if (team1_sum6_wins==3 and team1_sum6_draws==1 and team1_sum6_losses==2 and team2_sum6_wins==4 and team2_sum6_draws==1 and team2_sum6_losses==1 ):
        print("---> Οι γηπεδούχοι έχουν 3-1-2 και οι φιλοξενούμενοι 1-1-4 !!!  Άσσος!!!." )
      
      if (team1_sum6_wins==3 and team1_sum6_draws==1 and team1_sum6_losses==2):
        print("---> Οι γηπεδούχοι έχουν 3-1-2 !!!  Αυξημένες πιθανότητες νίκης για τους γηπεδούχους." ) 		
	 
      if (team2_sum6_wins==1 and team2_sum6_draws==1 and team2_sum6_losses==4):
        print("---> Οι φιλοξενούμενοι έχουν 1-1-4 !!! Προσοχή." )
      
      if (team2_sum6_wins==4 and team2_sum6_draws==1 and team2_sum6_losses==1):
        print("---> Οι φιλοξενούμενοι έχουν 4-1-1 !!! " )
	
      if (team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3):
        print("---> Οι φιλοξενούμενοι έχουν 1-2-3!!! Θα τα βρούν σκούρα." )
	
      
      if (team1_sum6_wins==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Νίκες!  Ίσως άσσος." )      
      if (team1_sum6_draws==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ισοπαλίες!  Ίσως Χ." )      
      if (team1_sum6_losses==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ήττες!  Ίσως 2πλό." )	
      if (team2_sum6_wins==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Νίκες!  Ίσως διπλό." )      
      if (team2_sum6_draws==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ισοπαλίες!  Ίσως Χ." )      
      if (team2_sum6_losses==0 ):
        print("---> Οι γηπεδούχοι έχουν 0 στις Ήττες!  Ίσως άσσος." )
      
      
      
	
      if (team1_sum6_wins==0 and team1_sum6_draws==2 and team1_sum6_losses==4 and team2_sum6_wins==1 and team2_sum6_draws==2 and team2_sum6_losses==3 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν  0 νίκες & οι φιλοξενούμενοι 1-2-3!!! Νίκη για {}.".format(team1_name))	
	
      if (team1_sum6_wins==3 and team1_sum6_draws==2 and team1_sum6_losses==1 and team2_sum6_wins==4 and team2_sum6_draws==2 and team2_sum6_losses==0 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν 3-2-1 & οι φιλοξενούμενοι 0 ήττες!!!  {} will win." .format(team1_name))	
	
      if (team1_sum6_wins==4 and team1_sum6_draws==0 and team1_sum6_losses==2 and team2_sum6_wins==4 and team2_sum6_draws==0 and team2_sum6_losses==2 ):
        print("---> Κριτήριο βιβλίου!!!: Οι γηπεδούχοι έχουν 4-0-2 & οι φιλοξενούμενοι 4-0-2!!! ΙΣΟΠΑΛΙΑ.")
        
          
      
      if (team1_sum5_wins==2 and team1_sum5_draws==1 and team1_sum5_losses==2):
    	  print("---> Φόρμα5 γηπεδούχων: 1Χ.")
      if (team2_sum5_wins==2 and team2_sum5_draws==2 and team2_sum5_losses==1):
        print("---> Φόρμα5 φιλοξενούμενων: 1Χ.")
        
      if (team1_sum5_wins==1 and team1_sum5_draws==2 and team1_sum5_losses==2):
        print("---> Φόρμα5 γηπεδούχων: Χ2.")
      if (team2_sum5_wins==1 and team2_sum5_draws==2 and team2_sum5_losses==2):
        print("---> Φόρμα5 φιλοξενούμενων: Χ2.")              
          
      if (team1_sum5_wins==2 and team1_sum5_draws==1 and team1_sum5_losses==2):
    	  print("---> Η φόρμα5 γηπεδούχων: 12.")
      if (team2_sum5_wins==2 and team2_sum5_draws==1 and team2_sum5_losses==2):
    	  print("---> Η φόρμα5 φιλοξενούμενων: 12.")    	  
    	  
    	  
      if (team2_sum6_wins==3 and team2_sum6_draws==1 and team2_sum6_losses==2):
       print("---> 3-1-2 για την ομάδα {}. Επικίνδυνο ματς, καλύτερα να το αποφύγουμε.".format(team2_name))  
    
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.5 and team1_int_avg_conceded<0.5 and team2_int_avg_conceded>2):
      	print("{}-{}. Οι γηπεδούχοι σκοράρουν κατα ριππάς και δέχεται γκολ με το σταγονόμετρο!!! Οι φιλοξενούμενοι δεν σκοράρουν και δέχονται πάνω απο 2 σε κάθε ματς!!!!!".format(team1_name,team2_name)) 
        
      if (team1_int_avg_scored>2 and team2_int_avg_scored<0.6 and team1_int_avg_conceded<0.7 and team2_int_avg_conceded>1.7):
      	print("{}-{}. Οι γηπεδούχοι σκοράρουν πάνω απο 2 γκολ σε κάθε ματς και δέχονται γκολ κάτω από 0.7. Οι φιλοξενούμενοι βάζουν γκολ <0.7 και δέχονται πάνω απο 2 σε κάθε ματς".format(team1_name,team2_name))   
      
      #if (team1_int_chance_to_score>80 and team2_int_chance_to_score<30 and team1_int_chance_to_concede<30 and team1_int_chance_to_concede>70):
      	#print("{}-{}. Οι γηπεδούχοι έχουν πάνω απο 80% να σκοράρουν στο προσεχές ματς και λιγότερο απο 30% να δεχτούν. Οι φιλοξενούμενοι δε σκοράρουν και δέχεται με ευκολία γκολ. Η γηπεδούχοι θα κερδίσουν!!!".format(team1_name,team2_name))
      
      if (team1_int_chance_to_score>69 and team2_int_chance_to_score<45 and team1_int_chance_to_concede<45 and team2_int_chance_to_concede>69):
      	print("{}-{}. Οι γηπεδούχοι έχουν πάνω απο 69% να σκοράρουν στο προσεχές ματς και λιγότερο απο 45% να δεχτούν. Οι φιλοξενούμενοι δε σκοράρουν και δέχεται με ευκολία γκολ. Η γηπεδούχοι θα κερδίσουν!!!".format(team1_name,team2_name)) 
      
      if (team1_int_chance_to_score<40 and team2_int_chance_to_score<40 and team1_int_chance_to_concede<40 and team2_int_chance_to_concede<40 and team1_last10_failtoscore_int>6 and team2_last10_failtoscore_int>6 and team1_last10_cleansheet_int>4 and team2_last10_cleansheet_int>4 and team1_int_avg_scored<1 and team2_int_avg_scored<1):
      	print("{}-{}. ΔΕ ΘΑ ΜΠΕΙ ΓΚΟΛ !!!!!!".format(team1_name,team2_name))
      if (team1_int_chance_to_score<50 and team2_int_chance_to_score<50 and team1_int_chance_to_concede<50 and team2_int_chance_to_concede<50 and team1_last10_failtoscore_int>5 and team2_last10_failtoscore_int>5 and team1_last10_cleansheet_int>5 and team2_last10_cleansheet_int>5 and team1_int_avg_scored<1 and team2_int_avg_scored<1):
      	print("{}-{}. UNDERάκι !!!!!!".format(team1_name,team2_name))
      
      if (team1_int_chance_to_score>69 and team2_int_chance_to_score>69 and team1_int_chance_to_concede>65 and team2_int_chance_to_concede>65 and team1_last10_failtoscore_int<3 and team2_last10_failtoscore_int<3 and team1_last10_cleansheet_int<3 and team2_last10_cleansheet_int<3 and team1_int_avg_scored>2 and team2_int_avg_scored>1.5):
      	print("{}-{}. Το παιχνίδι είναι BTTS και OVER !!!!!!".format(team1_name,team2_name))      
       
      print("")
      print("")
      
      print("###########*###################################*#######################################*##############################*##########################*############")    


