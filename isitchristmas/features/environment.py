from behave_webdriver.fixtures import fixture_browser

def before_all(context):
    fixture_browser(context)

def after_all(context):
    if hasattr(context, "behave_driver") and context.behave_driver:
        context.behave_driver.quit()
