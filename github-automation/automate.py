from selenium import webdriver
import os
import sys
import time

browser = webdriver.Chrome("drivers/chromedriver")
browser.get("https://github.com/login")


if len(sys.argv) == 2:

    RepoName = str(sys.argv[1])

    with open('github-automation/credentials.txt','r') as f:
        creds = f.readlines()

    username = creds[0].strip()
    password = creds[1].strip()

    browser.find_element_by_xpath("//input[@id='login_field']").send_keys(username)
    browser.find_element_by_xpath("//input[@id='password']").send_keys(password)
    browser.find_element_by_xpath("//input[@name='commit']").click()

    browser.get("https://github.com/"+username+"/"+RepoName)

elif len(sys.argv) == 3:

    ReqName = str(sys.argv[1])
    RepoName = str(sys.argv[2])

    browser.get("https://github.com/"+ReqName+"/"+RepoName)