from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    context.browser = webdriver.Chrome(options=options)
    context.browser.set_page_load_timeout(10)

def after_all(context):
    if hasattr(context, "browser") and context.browser:
        context.browser.quit()


#from behave_webdriver.fixtures import fixture_browser
#
#def before_all(context):
#    fixture_browser(context)
#
#def after_all(context):
#    if hasattr(context, "behave_driver") and context.behave_driver:
#        context.behave_driver.quit()
