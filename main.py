from selenium import webdriver
import time

PATH = r"C:\Users\Tatakae\Desktop\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://frs.gov.cz/en/ioff/application-status")

appnumber = driver.find_element_by_id('edit-ioff-application-number')
appnumber.send_keys('05194')

xxnumber = driver.find_element_by_id('edit-ioff-application-number-fake')
xxnumber.send_keys('04')

appcode = driver.find_element_by_xpath('//*[@id="edit-ioff-application-code"]/option[8]')
appcode.click()

appyear = driver.find_element_by_xpath('//*[@id="edit-ioff-application-year"]/option[2]')
appyear.click()
time.sleep(3)
verify = driver.find_element_by_id('edit-submit-button')
verify.click()

if "Approved" in driver.page_source:
    print("Congratulation, you visa is approved")
else:
    print(driver.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/ul/li[1]/p/span').text)
time.sleep(10)

driver.quit()
