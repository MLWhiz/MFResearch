# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

# Put your own username here

login_URL = "https://www.valueresearchonline.com/membership/getin.asp"
uname = "devrag1234@gmail.com"
pword = "curriculum"


URL = "https://www.valueresearchonline.com/funds/fundSelector/default.asp?cat=equityExcSec&exc=susp&exc=reg&exc=close&exc=3Star&exc=2Star&exc=1Star&x=9&y=11"

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2) 
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', '/Users/apple/ipython/vr')
fp.set_preference('browser.helperApps.neverAsk.openFile', 'text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml')
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml')
fp.set_preference('browser.helperApps.alwaysAsk.force', False)
fp.set_preference('browser.download.manager.alertOnEXEOpen', False)
fp.set_preference('browser.download.manager.focusWhenStarting', False)
fp.set_preference('browser.download.manager.useWindow', False)
fp.set_preference('browser.download.manager.showAlertOnComplete', False)
fp.set_preference('browser.download.manager.closeWhenDone', False)
                  
browser = webdriver.Firefox(fp)
browser.get(login_URL)
time.sleep(5)
print "Getting the login screen"
username = browser.find_element_by_id('username')
username.send_keys(uname)

password = browser.find_element_by_id('password')

password.send_keys(pword)
password.send_keys(Keys.RETURN)
time.sleep(5)

browser.get(URL)
time.sleep(15)

try:
    browser.find_element_by_id("noThanks").click()
except:
    pass
time.sleep(2)
print "clicked nothanks"

def download_page(browser,id):
    browser.find_element_by_id(id).click()
    print "clicked "+ id
    time.sleep(5)

    # open up the dropdown
    dropdown = browser.find_element_by_css_selector("div.dropdown-toggle")
    dropdown.click()

    # select element
    item = dropdown.find_element_by_xpath("//a[@id='downCsv']")
    item.click()
    time.sleep(2)
    print "clicked downcsv"

download_page(browser,"returns")
download_page(browser,"snapshot")
download_page(browser,"portfolio")
download_page(browser,"risk")
download_page(browser,"feesDetails")


