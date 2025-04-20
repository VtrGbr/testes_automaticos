from playwright.sync_api import sync_playwright
from time import sleep
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto('http://playwright.dev')
    
    print(page.title())
    
    browser.close()

