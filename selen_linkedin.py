from linkedin_scraper import Person, actions
from selenium import webdriver

from config import LINKEDIN_PASSWORD, LINKEDIN_EMAIL

driver = webdriver.Chrome()

email = LINKEDIN_EMAIL
password = LINKEDIN_PASSWORD
actions.login(driver, email, password)  # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/aibek-raiymbekov/", driver=driver)
print(person)
