import behave_webdriver
from behave_webdriver.steps import *

def before_all(context):
    # Create a headless Chrome driver
    driver = behave_webdriver.Chrome.headless()
    # Attach it under both names for compatibility
    context.behave_driver = driver
    context.browser = driver

def after_all(context):
    context.browser.quit()
