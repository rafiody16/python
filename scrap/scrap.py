import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



link_produk = time_target = None
sekarang = datetime.datetime.now()

# browser.get("nal-friendly-match-indonesia-vs-argentina?utm_page=toDoSearchResult")

def SetupSelenium():
    browser = webdriver.Chrome('D:\python\scrap\chromedriver')
    return browser

def inputData():
    global link_produk
    link_produk = input("link tiket: ")

def click(browser, element_css):
    WebDriverWait(browser,60). until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, ''))
    )
    WebDriverWait(browser, 60). until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, ''))
    )
    browser.find_element_by_css_selector(element_css).click()

inputData()
browser = SetupSelenium()
wait = WebDriverWait(browser, 120)
browser.get("https://www.tiket.com/login")
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#__next > main > div.index_main___rT19 > header > div > div:nth-child(7) > div > div > div > div.rr___Header-module__desktop_only___npH90.rr___Header-module__desktop_wrapper_without_bottom___nabMh > header > div > div.rr___HeaderDesktop-module__header_top___B8Fif > div.rr___HeaderDesktop-module__right___iAAHn > button.rr___UserModal-module__container___gjsZU > div > span > div')))
browser.get(link_produk)
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#__next > main > div.productSlug_responsive_wrapper__8isp2 > div > div:nth-child(6) > div > div.PackageSelection_package_wrapper__R7PMt > div:nth-child(2) > div.PackageSelection_package_list__jNZzL > div:nth-child(2) > div.C5DY4q_card_header.PackageSelection_package_header__rsSzm > div > h3')))
click(browser, '#__next > main > div.productSlug_responsive_wrapper__8isp2 > div > div:nth-child(6) > div > div.PackageSelection_package_wrapper__R7PMt > div:nth-child(2) > div.PackageSelection_package_list__jNZzL > div:nth-child(3) > div.PackageSelection_package_footer__nBjpQ > div > button')
# WebDriverWait(browser, 120). until(ec.invisibility_of_element((By.CSS_SELECTOR, '#__next > main > div.productSlug_responsive_wrapper__8isp2 > div > div:nth-child(6) > div > div.PackageSelection_package_wrapper__R7PMt > div:nth-child(2) > div.PackageSelection_package_list__jNZzL > div:nth-child(3) > div.PackageSelection_package_footer__nBjpQ > div > button > span:nth-child(2)')))
# click(browser, '#__next > main > div.productSlug_responsive_wrapper__8isp2 > div > div:nth-child(6) > div > div.PackageSelection_package_wrapper__R7PMt > div:nth-child(2) > div.PackageSelection_package_list__jNZzL > div:nth-child(3) > div.PackageSelection_package_footer__nBjpQ > div > button > span:nth-child(2)')


# buyButton = False
# while not buyButton:

#     try:
#         addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")
#         print("Button isnt ready")

#         time.sleep(1)
#         browser.refresh()

#     except:
#         addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
#         print("button was clicked")
#         addToCartBtn.click()
#         buyButton = True
