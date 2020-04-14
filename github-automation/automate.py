from selenium import webdriver
import os
import sys
import time

browser = webdriver.Chrome("PATH\ TO\ CHROMEDRIVER")
browser.get("https://github.com/login")

ReqName = str(sys.argv[1])
RepoName = str(sys.argv[2])

username = "USERNAME"
password = "PASSWORD"

browser.find_element_by_xpath("//input[@id='login_field']").send_keys(username)
browser.find_element_by_xpath("//input[@id='password']").send_keys(password)
browser.find_element_by_xpath("//input[@name='commit']").click()

browser.get("https://github.com/"+ReqName)

browser.get("https://github.com/"+ReqName+"/"+RepoName)