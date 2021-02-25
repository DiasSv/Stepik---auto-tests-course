import math
import time

from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"

try:

	browser = webdriver.Chrome()
	browser.get(link)

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	valuex = browser.find_element_by_id("treasure")
	x = valuex.get_attribute("valuex")


	y = calc(x)

	answer = browser.find_element_by_xpath("//div/input[@id = 'answer']")
	answer.send_keys(str(y))

	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()

	radiobut = browser.find_element_by_id("robotsRule")
	radiobut.click()

	button = browser.find_element_by_css_selector("div button.btn")
	button.click()

	time.sleep(2)
	time.sleep(10)

finally:

	browser.quit()