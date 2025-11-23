from behave import given, then
from selenium.webdriver.common.by import By

@given('I go to "https://downloadmoreram.com/"')
def step_open_download_page(context):
    context.behave_driver.get("https://downloadmoreram.com/")

@then('the title should contain "{text}"')
def step_title_contains(context, text):
    assert text.lower() in context.behave_driver.title.lower(), f'Title does not contain "{text}".'

@then('the page should contain the text "{text}"')
def step_page_contains_text(context, text):
    assert text.lower() in context.behave_driver.page_source.lower(), f'Text "{text}" not found on page.'

@then('there should be an element with tag name "{tag}"')
def step_element_with_tag(context, tag):
    elements = context.behave_driver.find_elements(By.TAG_NAME, tag)
    assert elements, f'No element with tag name "{tag}" found.'

@then('there should be at least 1 element with tag name "{tag}"')
def step_at_least_one_element_with_tag(context, tag):
    elements = context.behave_driver.find_elements(By.TAG_NAME, tag)
    assert len(elements) >= 1, f'Expected at least one element with tag name "{tag}", but found none.'

#