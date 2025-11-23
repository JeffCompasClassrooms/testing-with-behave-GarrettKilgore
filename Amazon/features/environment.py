import behave_webdriver
from behave_webdriver.steps import *

def before_all(context):
    # Run Chrome in headless mode
    context.browser = behave_webdriver.Chrome.headless()

def after_all(context):
    context.browser.quit()
