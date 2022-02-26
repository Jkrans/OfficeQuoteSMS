import sys
import keyring
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
chrome_prefs = {}
options.headless = True

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
url = 'https://www.officequotes.net/'
driver.get(url)

wait = WebDriverWait(driver, 30)

randomQuote = wait.until(EC.presence_of_element_located((By.ID, "random-quote")))
randomQuoteText = randomQuote.text

account_sid = keyring.get_password("twilio","account_sid")
auth_token = keyring.get_password("twilio","auth_token")
phoneNumber = keyring.get_password("JeremyKransInfo","phoneNumber")
ckPhoneNumber = keyring.get_password("ChristarKransInfo","phoneNumber")
fromNum = keyring.get_password("twilio","385NUM")

client = Client(account_sid, auth_token)

phoneNumbers = [phoneNumber , ckPhoneNumber]

for number in phoneNumbers:
    client.messages.create(
        to = number,
        from_ = fromNum,
        body = randomQuoteText
    )



print(randomQuoteText)

driver.quit()
sys.exit(0)