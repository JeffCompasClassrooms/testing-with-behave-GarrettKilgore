Feature: Amazon product search

  Scenario: Searching for a product on Amazon
    Given I am on the Amazon homepage
    When I click on the search bar
    And I type "wireless headphones"
    And I submit the search
    Then I should see results related to "wireless headphones"

  Scenario: Verifying search results contain keyword
    Given I am on the Amazon homepage
    When I search for "wireless headphones"
    Then the first 5 product titles should contain "headphones"

  Scenario: Sorting results by price
    Given I have searched for "wireless headphones" on Amazon
    When I open the sort menu
    And I select "Price: Low to High"
    And I wait for the page to refresh
    Then I should see products sorted from cheapest to most expensive

  Scenario: Viewing a product detail page
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should be taken to the product detail page
    And the product title should contain "headphones"

  Scenario: Checking product ratings
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should be taken to the product detail page
    And the product rating should be at least 4 stars

  Scenario: Viewing product specifications
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should see a section with technical specifications

  Scenario: Filtering results by customer rating
    Given I have searched for "wireless headphones" on Amazon
    When I apply the "4 Stars & Up" filter
    Then I should see only highly rated products

  Scenario: Navigating to the Electronics category
    Given I am on the Amazon homepage
    When I hover over the "All" menu
    And I click on "Electronics"
    Then I should see subcategories like "Headphones"

  Scenario: Checking product availability
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should see "In Stock" on the page

  Scenario: Reading customer reviews
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I scroll to the customer reviews section
    Then I should see reviews with star ratings

  Scenario: Checking delivery options
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    Then I should see estimated delivery dates

  Scenario: Viewing product specifications
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should see a section with technical specifications

Scenario: Checking product availability
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should see "In Stock" on the page

Scenario: Viewing customer questions and answers
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I scroll to the questions section
    Then I should see customer questions and answers

Scenario: Checking product shipping eligibility
    Given I have searched for "wireless headphones" on Amazon
    When I click on the first product
    And I wait for the product detail page to load
    Then I should see shipping eligibility information
