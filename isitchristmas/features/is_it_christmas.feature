Feature: Find out if it's Christmas or not
  As a person of celebration
  I want to know if it's Christmas
  So that I don't forget to celebrate.

  Scenario: It's not Christmas today
    Given I open the url "https://isitchristmas.com"
    Then I expect that element "a" contains the text "NO"

  Scenario: Homepage title should be correct
    Given I open the url "https://isitchristmas.com"
    Then I expect that the title contains the text "Is it Christmas?"

  Scenario: Page should contain NO
    Given I open the url "https://isitchristmas.com"
    Then I expect that the page contains the text "NO"

  Scenario: Page should not contain a form
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "form"

  Scenario: Page should not contain a search box
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with name "q"

  Scenario: Page should not have a header or footer
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with class name "header"
    Then I expect that there is no element with class name "footer"

  Scenario: Page should not have navigation links
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with tag name "nav"

  Scenario: Page should not have a login button
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with id "login"

  Scenario: Page should not have a signup link
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with link text "Sign Up"

  Scenario: Page should not have social media icons
    Given I open the url "https://isitchristmas.com"
    Then I expect that there is no element with class name "social"
