import time
from selenium import webdriver


sites = [ 'https://www.sahibinden.com/']


time_on_site =  60


wait_time = 2 * 60 * 60

while True:
    
    browser = webdriver.Chrome()
    
    for site in sites:
        
        browser.get(site)
        
        
        time.sleep(time_on_site)
        
        
        browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(5)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    
    
    browser.close()
    
    
    time.sleep(wait_time)

