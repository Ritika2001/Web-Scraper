
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get('https://www.linkedin.com/feed/update/urn:li:activity:6529748704885342208/')
time.sleep(60)

COMMENTS_XPATH = '/html/body/div[5]/div[6]/div[3]/div/div/div/div/div/section/div[1]/div[7]/div[3]/div/button'

while True:
    try:
        loadMoreButton = driver.find_element_by_xpath(COMMENTS_XPATH)
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        break
print "Complete loading all comments"

time.sleep(60)

comments = pd.DataFrame(columns = ['user_names','messages']) 

boxes = driver.find_elements_by_xpath("//*[contains(@class, 'comments-comments-list__comment-item comments-comment-item ember-view')]")

comment_boxes = []
for i in boxes:
	comment_boxes.append(i.get_attribute('id'))

for x in comment_boxes:
	user_name = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div[2]/a[2]/h3/span[1]/span')[0]
	name = user_name.text

	try:
		user_message = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div[3]/.//a')[0]
		message = user_message.text
	except:
		message = ''

	comments.loc[len(comments)] = [name, message]

print(comments)
