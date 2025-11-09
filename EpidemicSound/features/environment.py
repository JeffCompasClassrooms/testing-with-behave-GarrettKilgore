import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

def before_all(context):
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()

@given("I visit Epidemic Sound")
def step_visit_homepage(context):
    context.driver.get("https://www.epidemicsound.com/")

@when('I search for "{term}"')
def step_search_for_term(context, term):
    music_link = context.driver.find_element(By.LINK_TEXT, "Music")
    music_link.click()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
    )
    search_input = context.driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    search_input.send_keys(term)
    search_input.send_keys(Keys.RETURN)

@then('I should see the tagline "{text}"')
def step_see_tagline(context, text):
    assert text in context.driver.page_source

@then('I should see results related to "{term}"')
def step_verify_search_results(context, term):
    assert term.lower() in context.driver.page_source.lower()

@when('I filter by genre "{genre}"')
def step_filter_by_genre(context, genre):
    genre_button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{genre}')]")
    genre_button.click()

@then('I should see tracks labeled "{label}"')
def step_verify_genre_label(context, label):
    assert label.lower() in context.driver.page_source.lower()
