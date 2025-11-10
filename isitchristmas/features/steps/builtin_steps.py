from behave_webdriver.steps import *
from behave import then
from selenium.webdriver.common.by import By


@then('I expect that the page contains the text "{text}"')
def step_page_contains_text(context, text):
    assert text in context.behave_driver.page_source, f'Text "{text}" not found on page.'

@then('I expect that the title contains the text "{text}"')
def step_title_contains_text(context, text):
    assert text in context.behave_driver.title, f'Title does not contain "{text}".'

@then('I expect that there is no element with tag name "{tag}"')
def step_no_element_with_tag(context, tag):
    elements = context.behave_driver.find_elements(By.TAG_NAME, tag)
    assert len(elements) == 0, f'Unexpected element with tag name "{tag}" found.'

@then('I expect that there is no element with class name "{class_name}"')
def step_no_element_with_class_name(context, class_name):
    elements = context.behave_driver.find_elements(By.CLASS_NAME, class_name)
    assert len(elements) == 0, f'Unexpected element with class name "{class_name}" found.'

@then('I expect that there is no element with id "{element_id}"')
def step_no_element_with_id(context, element_id):
    elements = context.behave_driver.find_elements(By.ID, element_id)
    assert len(elements) == 0, f'Unexpected element with id "{element_id}" found.'

@then('I expect that there is no element with attribute "name" and value "{value}"')
def step_no_element_with_name_attribute(context, value):
    elements = context.behave_driver.find_elements(By.NAME, value)
    assert len(elements) == 0, f'Unexpected element with name="{value}" found.'
