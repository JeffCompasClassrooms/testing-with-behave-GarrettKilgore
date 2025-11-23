from behave import given, when, then
from selenium.webdriver.common.by import By
from behave_webdriver.steps import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open the instructables peppers ghost page")
def step_open_page(context):
    context.browser.get("https://www.instructables.com/Peppers-Ghost-Illusion-in-a-Small-Space/")

@when('I scroll to the section containing "{text}"')
def step_scroll_to_section(context, text):
    element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", element)

@then('I expect that there is at least one picture there')
def step_check_for_picture(context):
    images = context.browser.find_elements(By.CSS_SELECTOR, "img")
    assert images, "No images found on the page"

@then('the page should contain the text "{text}"')
def step_page_contains_text(context, text):
    assert text.lower() in context.browser.page_source.lower(), f'Text "{text}" not found on page.'

@then('the title should contain "{text}"')
def step_title_contains_text(context, text):
    assert text.lower() in context.browser.title.lower(), f'Title does not contain "{text}".'

@then('there should be no element with {locator_type} "{value}"')
def step_no_element_by(context, locator_type, value):
    locator_map = {
        "id": By.ID,
        "name": By.NAME,
        "class name": By.CLASS_NAME,
        "tag name": By.TAG_NAME,
        "link text": By.LINK_TEXT
    }
    by = locator_map.get(locator_type)
    assert by, f'Unsupported locator type: {locator_type}'
    elements = context.browser.find_elements(by, value)
    assert len(elements) == 0, f'Element with {locator_type} "{value}" was found.'

@then('there should be no element with attribute "{attr}" and value "{value}"')
def step_no_element_with_attribute(context, attr, value):
    elements = context.browser.find_elements(By.XPATH, f'//*[@{attr}="{value}"]')
    assert len(elements) == 0, f'Element with {attr}="{value}" was found.'
