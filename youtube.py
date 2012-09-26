from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process
import time
import os

dir(webdriver)

#browser = webdriver.Chrome() # Get local session of chrome
#browser.get("http://www.youtube.com/watch?v=CgS_QmWBlhc&feature=youtu.be") # Load page
#time.sleep(1) # Let the page load, will be added to the API

view_count = 0
def viewVideo():
    try:
        view_count = 0
        if view_count == 0:
            browser = webdriver.Chrome() # Get local session of chrome
            browser.get("http://www.youtube.com/watch?v=AokLz3QOcFc&feature=plcp") # Load page
            time.sleep(1) # Let the page load, will be added to the API
            actionpanel = browser.find_elements_by_xpath("//div[@id='watch-actions-share-panel']")
            emailbutton = actionpanel[0].find_elements_by_xpath("//button[@type='button']")
            time.sleep(1)
            emailbutton[0].click()
            inputemail = browser.find_elements_by_xpath("//input[@id='Email']")
            inputpassword = browser.find_elements_by_xpath("//input[@id='Passwd']")
            inputemail[0].send_keys("dummytestingpurpose")
            inputpassword[0].send_keys("letstest")
            signin = browser.find_elements_by_xpath("//input[@id='signIn']")
            signin[0].click()
            #elem = browser.find_elements_by_xpath("//div[@id='watch-actions']")
            #button = elem[0].find_elements_by_xpath("//button[@id='watch-share']")
            #button[0].click()
            #time.sleep(2)
            #span = browser.find_element_by_xpath("//span[@class='share-panel-main-buttons']/button[2]")
            #span.click()
            #time.sleep(2)
            #textarea = browser.find_element_by_xpath("//div[@id='watch-actions-share-panel']/div/div/div[4]/div")
            #forms = textarea.find_elements_by_xpath("//form[@action='/share_ajax?action_send_email=1']")
            #emailtextarea = forms[0].find_elements_by_xpath("//textarea[@name='recipients']")
            #emailtextarea[0].send_keys("karthikjagadeesh@gmail.com")
            time.sleep(70)
            browser.quit()
            view_count = view_count + 1
            #print "time: ", time.ctime(),'process id:', os.getpid(), "view_count: ", view_count
            
        #forms[0].submit()
        #print "Video Shared"
        #cookies = browser.get_cookies()
       # for c in cookies:
        #	print c
    except NoSuchElementException:
        assert 0, "can't find seleniumhq"
    #browser.close()

if __name__ == '__main__':
    while 1:
        process_count = 0
        process_list = []
        while process_count < 10:
            p = Process(target=viewVideo)
            p.start()
            time.sleep(5)
            process_list.append(p)
            process_count = process_count + 1
        for p in process_list:
            p.join()
        view_count = view_count+process_count
        print "view_count: " + str(view_count)
        for p in process_list:
            p.terminate()

