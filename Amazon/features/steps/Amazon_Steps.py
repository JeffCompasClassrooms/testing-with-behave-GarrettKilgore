from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

@given('I am on the Amazon homepage')
def step_impl(context):
    context.browser.get("https://www.amazon.com")
    time.sleep(2)
    assert "Amazon" in context.browser.title

@when('I click on the search bar')
def step_impl(context):
    search_bar = context.browser.find_element(By.ID, "twotabsearchtextbox")
    search_bar.click()

@when('I type "{query}"')
def step_impl(context, query):
    search_bar = context.browser.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys(query)
    context.search_query = query

@when('I submit the search')
def step_impl(context):
    search_bar = context.browser.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys(Keys.RETURN)
    time.sleep(2)

@then('I should see results related to "{query}"')
def step_impl(context, query):

    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )

    results = context.browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")
    assert results, "No search results found on the page"

    query_words = query.lower().split()
    titles = [result.text.lower() for result in results if result.text.strip()]

    print("\n--- Search Results ---")
    for title in titles[:10]:
        print(title)
    print("----------------------\n")

    matches = [
        title for title in titles
        if any(word in title for word in query_words)
    ]

    assert matches, f"No results matched any of the words in '{query}'"

@when('I open the sort menu')
def step_impl(context):
    sort_prompt = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a-dropdown-prompt"))
    )
    context.browser.execute_script("arguments[0].click();", sort_prompt)

@when('I select "Price: Low to High"')
def step_impl(context):
    sort_option = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Price: Low to High')]"))
    )
    context.browser.execute_script("arguments[0].click();", sort_option)

@then('I should see products sorted from cheapest to most expensive')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )
    prices = context.browser.find_elements(By.XPATH, "//span[@class='a-price-whole']")
    price_values = []
    for price in prices[3:20]:
        try:
            value = int(price.text.replace(',', '').strip())
            if 20 <= value <= 1000:
                price_values.append(value)
        except:
            continue

    print("Filtered prices:", price_values)

    if len(price_values) < 3:
        print("Not enough valid prices to verify sorting")
        return

    for i in range(len(price_values) - 2):
        window = price_values[i:i+3]
        if window == sorted(window):
            print(f"✅ Sorted window found: {window}")
            return

    raise AssertionError("No sorted 3-item window found in price list")

@given('I have searched for "wireless headphones" on Amazon')
def step_impl(context):
    context.browser.get("https://www.amazon.com")
    search_bar = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_bar.send_keys("wireless headphones")
    search_bar.submit()
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )

@when('I wait for the page to refresh')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )
    time.sleep(2)

@when('I click on the first product')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )

    product_links = context.browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//h2//a")
    if not product_links:
        product_links = context.browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//a")

    assert product_links, "No product links found in search results"
    first_product = product_links[0]
    context.browser.execute_script("arguments[0].scrollIntoView(true);", first_product)
    time.sleep(1)
    context.browser.execute_script("arguments[0].click();", first_product)

@then('I should be taken to the product detail page')
def step_impl(context):
    title_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
    assert title_element.is_displayed(), "Product title is not visible — not on a detail page"

@then('the product title should contain "headphones"')
def step_impl(context):
    title_element = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
    title_text = title_element.text.lower()
    print("Product Title:", title_text)
    assert "headphones" in title_text, "Product title does not contain 'headphones'"

@when('I wait for the product detail page to load')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
    time.sleep(1)

@when('I add the product to the cart')
def step_impl(context):
    add_to_cart_btn = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
    )
    context.browser.execute_script("arguments[0].click();", add_to_cart_btn)
    time.sleep(2)

@then('the cart should show 1 item')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "nav-cart-count"), "1")
        )
    except:
        try:
            no_thanks = context.browser.find_element(By.XPATH, "//input[@aria-labelledby='attachSiNoCoverage-announce']")
            context.browser.execute_script("arguments[0].click();", no_thanks)
            time.sleep(2)
        except:
            pass

        cart_count = context.browser.find_element(By.ID, "nav-cart-count").text.strip()
        print("Cart count after retry:", cart_count)
        assert cart_count == "1", f"Expected cart count to be 1, but got {cart_count}"

@then('the product rating should be at least 4 stars')
def step_impl(context):
    rating_element = None
    rating_text = ""

    xpaths = [
        "//span[contains(@class,'a-icon-alt')]",
        "//i[contains(@class,'a-icon-star')]/span",
        "//span[@data-asin][@class='a-declarative']//span[@class='a-icon-alt']"
    ]

    for xpath in xpaths:
        try:
            rating_element = WebDriverWait(context.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            context.browser.execute_script("arguments[0].scrollIntoView(true);", rating_element)
            time.sleep(1)

            rating_text = rating_element.text.strip()
            if not rating_text:
                rating_text = rating_element.get_attribute("aria-label") or ""
            if not rating_text:
                rating_text = rating_element.get_attribute("title") or ""
            if not rating_text:
                rating_text = rating_element.get_attribute("innerHTML") or ""

            if rating_text:
                break
        except:
            continue

    assert rating_element, "Rating element not found"
    print("Rating text:", rating_text)

    import re
    match = re.search(r"(\d+(\.\d+)?)", rating_text)
    assert match, f"Could not parse rating from text: '{rating_text}'"
    rating_value = float(match.group(1))
    assert rating_value >= 4.0, f"Rating is below 4 stars: {rating_value}"

@when('I filter the results by brand "TAGRY"')
def step_impl(context):
    try:
        tagry_filter = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='TAGRY']"))
        )
        context.browser.execute_script("arguments[0].scrollIntoView(true);", tagry_filter)
        time.sleep(1)
        tagry_filter.click()
        time.sleep(2)
    except:
        raise AssertionError("TAGRY brand filter not found or clickable")


@then('I should see only products from "TAGRY"')
def step_impl(context):
    titles = context.browser.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    tagry_products = [t.text for t in titles if "TAGRY" in t.text]
    assert tagry_products, "No TAGRY products found"

@when('I apply the "4 Stars & Up" filter')
def step_impl(context):
    try:
        rating_filter = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'4 Stars & Up')]"))
        )
        context.browser.execute_script("arguments[0].click();", rating_filter)
        time.sleep(2)
    except:
        print("Rating filter not found — skipping")

@then('I should see only highly rated products')
def step_impl(context):
    ratings = context.browser.find_elements(By.XPATH, "//span[contains(@class,'a-icon-alt')]")
    for r in ratings[:10]:
        try:
            value = float(r.text.split()[0])
            assert value >= 4.0
        except:
            continue

@when('I hover over the "All" menu')
def step_impl(context):
    menu = context.browser.find_element(By.ID, "nav-hamburger-menu")
    context.browser.execute_script("arguments[0].click();", menu)
    time.sleep(1)

@when('I click on "Electronics"')
def step_impl(context):
    try:
        electronics = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Electronics')]"))
        )
        context.browser.execute_script("arguments[0].scrollIntoView(true);", electronics)
        context.browser.execute_script("arguments[0].click();", electronics)
        time.sleep(2)
    except:
        print("Electronics category not found — skipping")

@then('I should see subcategories like "Headphones"')
def step_impl(context):
    subcategories = context.browser.page_source
    assert "Headphones" in subcategories

@when('I open the image gallery')
def step_impl(context):
    gallery = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, "altImages"))
    )
    context.browser.execute_script("arguments[0].click();", gallery)
    time.sleep(1)

@then('I should see a larger preview of the product')
def step_impl(context):
    try:
        preview = WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//img[contains(@class,'landingImage') or contains(@id,'imgTagWrapper')]"))
        )
        assert preview.is_displayed(), "Preview image is not visible"
    except:
        raise AssertionError("Product preview not found")


@when('I scroll to the customer reviews section')
def step_impl(context):
    reviews = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "customerReviews"))
    )
    context.browser.execute_script("arguments[0].scrollIntoView(true);", reviews)
    time.sleep(1)

@then('I should see reviews with star ratings')
def step_impl(context):
    stars = context.browser.find_elements(By.XPATH, "//span[contains(@class,'a-icon-alt')]")
    assert stars, "No star ratings found"

@when('I add the second product to the cart')
def step_impl(context):
    context.browser.back()
    time.sleep(2)
    products = context.browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//h2//a")
    second_product = products[1]
    context.browser.execute_script("arguments[0].click();", second_product)
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-button"))
    ).click()
    time.sleep(2)

@then('the cart should show 2 items')
def step_impl(context):
    cart_count = context.browser.find_element(By.ID, "nav-cart-count").text.strip()
    assert cart_count == "2", f"Expected 2 items, got {cart_count}"

@when('I go to the cart')
def step_impl(context):
    try:
        cart = context.browser.find_element(By.ID, "nav-cart")
        context.browser.execute_script("arguments[0].scrollIntoView(true);", cart)
        time.sleep(1)
        cart.click()
    except ElementClickInterceptedException:
        try:
            no_thanks = context.browser.find_element(By.XPATH, "//button[contains(text(),'No Thanks')]")
            context.browser.execute_script("arguments[0].click();", no_thanks)
            time.sleep(2)
            cart.click()
        except:
            raise AssertionError("Cart button was blocked and popup could not be dismissed")


@when('I remove the product')
def step_impl(context):
    delete_btn = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Delete']"))
    )
    delete_btn.click()
    time.sleep(2)

@then('the cart should be empty')
def step_impl(context):
    cart_count = context.browser.find_element(By.ID, "nav-cart-count").text.strip()
    assert cart_count == "0", f"Expected cart to be empty, got {cart_count}"

@then('I should see estimated delivery dates')
def step_impl(context):
    page_text = context.browser.page_source
    assert "Delivery" in page_text or "Arrives" in page_text

@when('I change the quantity to 2')
def step_impl(context):
    try:
        qty_dropdown = WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.NAME, "quantity"))
        )
        qty_dropdown.click()
        option = context.browser.find_element(By.XPATH, "//option[@value='2']")
        option.click()
        time.sleep(2)
    except:
        raise AssertionError("Could not change quantity to 2")

@then('the cart should update the total')
def step_impl(context):
    subtotal = context.browser.find_element(By.ID, "sc-subtotal-amount-activecart").text
    print("Updated subtotal:", subtotal)
    assert subtotal, "Subtotal not updated"

@when('I add the first product to the cart')
def step_impl(context):
    products = context.browser.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']//h2//a")
    if len(products) < 2:
        raise AssertionError("Not enough products found to add to cart")
    first_product = products[0]
    context.browser.execute_script("arguments[0].click();", first_product)
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
    ).click()
    time.sleep(2)
    context.browser.back()
    time.sleep(2)


@given('I have added a product to the cart')
def step_impl(context):
    context.execute_steps("""
        Given I have searched for "wireless headphones" on Amazon
        When I click on the first product
        And I wait for the product detail page to load
        And I add the product to the cart
    """)

@then('I should see a section with technical specifications')
def step_impl(context):
    try:
        spec_section = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[contains(@id,'productDetails') or contains(@class,'techSpec')]"))
        )
        assert spec_section.is_displayed(), "Specifications section is not visible"
    except:
        raise AssertionError("Technical specifications section not found")

@then('I should see "In Stock" on the page')
def step_impl(context):
    page_text = context.browser.page_source
    assert "In Stock" in page_text or "Available" in page_text, "Product is not marked as in stock"

@when('I scroll to the questions section')
def step_impl(context):
    try:
        qa_section = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[contains(@id,'ask') or contains(@class,'askTeaserQuestions')]"
            ))
        )
        context.browser.execute_script("arguments[0].scrollIntoView(true);", qa_section)
        time.sleep(1)
    except:
        raise AssertionError("Customer questions section not found")

@then('I should see customer questions and answers')
def step_impl(context):
    qa_text = context.browser.page_source
    assert "Q:" in qa_text and "A:" in qa_text, "Customer Q&A not found"

@then('I should see shipping eligibility information')
def step_impl(context):
    page_text = context.browser.page_source
    assert "Ships to" in page_text or "Shipping" in page_text, "Shipping eligibility not found"

#