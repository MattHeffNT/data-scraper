# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

userInput = input("what would you like to search for from ANU data commons? ")


url = f"https://datacommons.anu.edu.au/DataCommons/rest/search/?q={userInput}&limit=20"

driver.get(url)

driver.implicitly_wait(0.5)


text_box = driver.find_element(by=By.ID, value="idBasicSearchTerms")
submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='GO']")


# text_box.send_keys("test")

driver.implicitly_wait(0.5)
# submit_button.click()
