'''Code to search for open visa appointment spots at Slovakian Embassies'''

#Necessary drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
import requests

#Website login details and other variables
app_num = '[username]'
pass_num = '[passport number]'
good_slots = ['[0/5]', '[1/5]', '[2/5]', '[3/5]', '[4/5]'] #In future, this should be done with RegEx

#Telegram id and message definitions. The details of the Telegram bot to send the message to if an open slot is found.
token = "[Telegram token]"
chat_id = "[Telegram chat id]"
message = "Date available at the XXX consulate - log in now!"
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

#While loop that does the scraping/search for a vis appointment
while True:
	#Opening webpage
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
	driver.get("https://ezov.mzv.sk/e-zov/dateOfVisitDecision.do?siteLanguage=")

	#Input to application number box
	app_box = driver.find_element(By.NAME, 'j_username')
	app_box.send_keys(app_num)

	#Input to passport number box
	pass_box = driver.find_element(By.NAME, 'j_password')
	pass_box.send_keys(pass_num)

	#Press login button
	driver.find_element(By.CLASS_NAME, 'pointer').click()

	#Make reservation and choose consulate
	driver.find_element(By.CLASS_NAME, 'navigationLink').click()
	consulate = Select(driver.find_element(By.ID, 'calendar.consularPost.consularPost'))
	consulate.select_by_visible_text('Moscow')
	driver.find_element(By.CLASS_NAME, 'pointer').click()

	#Find empty slot
	check_dates = str(driver.find_element(By.TAG_NAME, "body").text)
	slot_available = False
	if any(slot in check_dates for slot in good_slots):
		slot_available = True
	else:
		while True:
			driver.find_element(By.ID, "nextMonthLabel").click()
			check_dates = str(driver.find_element(By.TAG_NAME, "body").text)
			if "02/2023" in check_dates:
				break
			elif any(slot in check_dates for slot in good_slots):
				slot_available = True
				break

	#Send message if slot opens up
	if slot_available:
		print(requests.get(url).json())

	#Close browser
	driver.quit()

	#Run again in 3 mins
	time.sleep(180)