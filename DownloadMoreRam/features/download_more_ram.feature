Feature: Explore the DownloadMoreRAM.com site
  As a curious user
  I want to interact with the site
  So that I can verify its structure and humor

  Scenario: Load the homepage successfully
    Given I go to "https://downloadmoreram.com/"
    Then the title should contain "DownloadMoreRAM.com - CloudRAM 2.0"
    And the page should contain the text "Instant, Fast, FREE"
    And the page should contain the text "Download"
    And the page should contain the text "RAM"

  Scenario: Verify RAM options are listed
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "4 GB"
    And the page should contain the text "8 GB"
    And the page should contain the text "16 GB"
    And the page should contain the text "32 GB"

  Scenario: Confirm presence of navigation links
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "Home"
    And the page should contain the text "Download"
    And the page should contain the text "Shop"
    And the page should contain the text "Contact"

  Scenario: Validate merchandise section
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "Need a T-Shirt?"
    And the page should contain the text "See More!"
    And the page should contain the text "Zazzle"
    And the page should contain the text "Select Plan"

  Scenario: Check for contact information
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "Contact Us"
    And the page should contain the text "info@downloadmoreram.com"
    And the page should contain the text "1800-DOWNLOAD-MORE-RAM"
    And the page should contain the text "Twitter"

  Scenario: Validate footer humor content
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "This isn't a scam"
    And the page should contain the text "Please select the amount of RAM you would like to download"
    And the page should contain the text "CloudRAM 2.0"
    And the page should contain the text "One cannot simply Download too much RAM."

  Scenario: Verify page structure
    Given I go to "https://downloadmoreram.com/"
    Then there should be an element with tag name "header"
    Then the page should contain the text "This isn't a scam"
    Then there should be an element with tag name "header"
    And there should be an element with tag name "nav"

  Scenario: Check for images
    Given I go to "https://downloadmoreram.com/"
    Then there should be at least 1 element with tag name "img"
    And the page should contain the text "Download"
    And the page should contain the text "RAM"

  Scenario: Verify download section
    Given I go to "https://downloadmoreram.com/"
    Then the page should contain the text "Download"
    And the page should contain the text "DDR4-2400"
    And the page should contain the text "Download"
    And the page should contain the text "Instant"

  Scenario: Validate favicon and branding elements
    Given I go to "https://downloadmoreram.com/"
    Then the title should contain "DownloadMoreRAM.com"
    And there should be at least 1 element with tag name "link"
    And the page should contain the text "Download"
    And the page should contain the text "CloudRAM 2.0"
