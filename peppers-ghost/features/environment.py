import os
import behave_webdriver
from behave_webdriver.steps import *

def before_all(context):
    if os.getenv("BEHAVE_HEADLESS", "true").lower() == "true":
        driver = behave_webdriver.Chrome.headless()
    else:
        driver = behave_webdriver.Chrome()
    context.browser = driver
    context.behave_driver = driver

def after_all(context):
    context.browser.quit()
