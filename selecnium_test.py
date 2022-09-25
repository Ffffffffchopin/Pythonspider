from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_optimes=Options()
chrome_optimes.add_argument("--incognito")
chrome_optimes.add_argument("--Windows-size=1920x1080")

drive=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_optimes)
executable='C:\\Program Files\\Google\\Chrome\\chromedriver.exe'
url='https://architizer.com/projects/q/'
drive.get(url)

try:
    element = WebDriverWait(drive, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img-holder"))
    )
finally:
    drive.quit()