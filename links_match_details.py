import sys
import requests
from selenium import webdriver
import time
##################################😎 ΔΗΜΙΟΥΡΓΕΙ ΝΕΑ ΛΙΝΚΣ ΓΙΑ ΤΑ MATCH DETAILS ΜΕΣΑ ΣΤΑ ΟΠΟΙΑ ΘΑ ΒΡΟΥΜΕ ΤΑ ΠΕΝΑΛΤΥ ΚΑΙ ΤΑ ΑΥΤΟΓΚΟΛ #################################

#ΕΔΩ ΔΙΝΟΥΜΕ ΗΜΕΡΟΜΗΝΙΑ ΑΓΩΝΑ
year= input("Year:")
year1=str(year)
month= input("Month:")
month1=str(month)
day= input("Day:")
day1=str(day)
slash='/'

with open("links.txt") as istr:
    with open("links-penalty.txt", "w") as ostr:
        for i,line in enumerate (istr):
	        	line = line.rstrip('\n')
	        	newline=line.replace("compare","match")
	        	newline1=newline.replace("teams","info")
	        	line = "{}{}{}-{}-{}".format(newline1,slash,year1,month1,day1)
	        	print(line, file=ostr)