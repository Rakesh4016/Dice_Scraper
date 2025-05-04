from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def restart_driver():
    chrome_options = Options()
    
    # 🟢 Show browser for local testing
    # chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # use webdriver-manager to fetch the right driver
    service = Service(ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service, options=chrome_options)
    wait    = WebDriverWait(driver, 10)
    return driver, wait
