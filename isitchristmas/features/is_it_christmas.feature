Feature: Find out if it's Christmas or not
  As a person of celebration
  I want to know if it's Christmas
  So that I don't forget to celebrate.

  Scenario: Load the homepage
    Given I open the url "https://isitchristmas.com"
    Then I expect that the page contains the text "NO"

  Scenario: Verify page title
    Given I open the url "https://isitchristmas.com"
    Then I expect that the title contains the text "Is it Christmas?"

  Scenario: Confirm single-word response
    Given I open the url "https://isitchristmas.com"
    Then I expect that element "a" contains the text "NO"

  Scenario: Ensure no interactive elements
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "form"
    And I expect that there is no element with tag name "button"

  Scenario: Confirm minimalist layout
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "nav"
    And I expect that there is no element with class name "footer"

  Scenario: Page should not contain a login form
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with id "login"
    And I expect that there is no element with tag name "form"

  Scenario: Page should not contain navigation links
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "nav"
    And I expect that there is no element with class name "menu"

  Scenario: Page should not contain social media icons
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with class name "social"
    And I expect that there is no element with class name "share"

  Scenario: Page should not contain a footer
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "footer"
    And I expect that there is no element with class name "footer"

  Scenario: Page should not contain a search box
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with attribute "name" and value "q"
    And I expect that there is no element with tag name "input"
