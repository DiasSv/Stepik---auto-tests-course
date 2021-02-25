import time

from selenium import webdriver
link = "http://suninjuly.github.io/math.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	people_radio = browser.find_element_by_id("robotsRule")

	people_checked = people_radio.get_attribute("checked")

	print("значение людей-радио:  ", people_checked)
	assert people_checked is None

finally:

	browser.quit()