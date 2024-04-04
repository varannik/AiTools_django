'''
Create new selenium remote driver
'''
from selenium import webdriver
from bs4 import BeautifulSoup

def createDriver(URL, URL_SELENIUM, enableCookies=False):
  '''Return driver'''

  options = webdriver.ChromeOptions()
  if enableCookies:
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
  driver = webdriver.Remote(command_executor=URL_SELENIUM, options=options)

  driver.get(URL)

  return driver



def soupParser(driver):
  '''return page source by BeautifulSoup'''

  soup = BeautifulSoup(driver.page_source, features="html.parser")

  return soup


def exportHTML(driver):
  
  with open("source.html", "w", encoding='utf-8') as f:
    f.write(driver.page_source)