# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()
    )
)

userInput = input("what would you like to search for from ANU data commons? ")

# search using user input and rest
url = ("https://datacommons.anu.edu.au/DataCommons"
       f"/rest/search/?q={userInput}&limit=200")

driver.get(url)

driver.implicitly_wait(1)

# select articles from search
articles = driver.find_elements(By.TAG_NAME, value="article")


# loop through returned search items
for element in articles:

    driver.implicitly_wait(1)

    # find the link in the article
    link = element.find_element(By.TAG_NAME, value="a")

    driver.implicitly_wait(1)

    # open the article in a new tab
    link.send_keys(Keys.CONTROL + Keys.RETURN)

    # remove from the loop list so that when we navigate back loop goes to next article
    driver.execute_script("document.querySelector('article')"
    ".style = 'display:none;'")

    # switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    driver.implicitly_wait(1)

    data = driver.find_element(By.CLASS_NAME, value="col-9")

    print(data.text)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
