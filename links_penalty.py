import sys
import requests
from selenium import webdriver
import time
##################################😎 PARE TA LINKS HEAD 2 HEAD #########################################


with open("links.txt") as f:
    with open("links-penalty.txt", "w") as f1:
        for line in f:
        	f1.write(line)

year= input("Year:")
year1=str(year)
month= input("Month:")
month1=str(month)
day= input("Day:")
day1=str(day)
slash='/'
with open("links-penalty.txt", "r") as f2:
	with open("links_penalty1.txt", "w") as f3:
		for line in f2:
			newline=line.replace("compare","match")
			newline1=newline.replace("teams","info")
			f3.write("{}{}{}-{}-{}".format(newline1,slash,year1,month1,day1))