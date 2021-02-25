import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:

	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html")

	num1 = browser.find_element_by_id("num1").text
	num2 = browser.find_element_by_id("num2").text

	calc = int(num2) + int(num1)
	calc = str(calc)


	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_value(calc)

	button = browser.find_element_by_css_selector("form>button.btn").click()
	

finally:

	time.sleep(5)
	browser.quit()