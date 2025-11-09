Feature: Explore Epidemic Sound's music discovery and licensing platform
  As a creative user
  I want to interact with the site
  So that I can verify its music search, playback, and licensing features

  Scenario: Load the homepage
    Given I visit Epidemic Sound
    Then I should see the tagline "Bring your story to life"
    And I should see a call to action to "Create free account"
    And I should see a navigation link for "Music"
    And I should see a navigation link for "Sound effects"

  Scenario: Search for a track by keyword
    Given I visit Epidemic Sound
    When I search for "lofi"
    Then I should see results related to "lofi"
    And I should see a genre filter option
    And I should see a mood filter option

  Scenario: Filter tracks by genre
    Given I visit Epidemic Sound
    When I search for "beats"
    And I filter by genre "Hip Hop"
    Then I should see tracks labeled "Hip Hop"
    And I should see a genre tag in the results

  Scenario: Filter tracks by mood
    Given I visit Epidemic Sound
    When I search for "cinematic"
    And I filter by mood "Epic"
    Then I should see tracks with an epic mood
    And I should see mood tags in the results

  Scenario: Preview a track
    Given I search for "ambient"
    When I click play on the first track
    Then I should hear the track preview
    And I should see the playback bar moving

  Scenario: Add a track to favorites
    Given I search for "electronic"
    When I mark the first track as favorite
    Then the track should appear in my favorites list

  Scenario: Explore sound effects
    Given I visit Epidemic Sound
    When I navigate to the "Sound effects" section
    Then I should see categories like "Nature" and "Urban"
    And I should see a search bar for sound effects

  Scenario: Search for a sound effect
    Given I visit the sound effects section
    When I search for "rain"
    Then I should see sound effects related to "rain"
    And I should see duration labels on each result

  Scenario: View artist profile
    Given I search for "Ooyy"
    When I click on the artist name
    Then I should see the artist's profile page
    And I should see a list of their tracks

  Scenario: Explore curated playlists
    Given I visit Epidemic Sound
    When I navigate to the "Browse" section
    Then I should see curated playlists
    And I should see playlist titles like "Creator Favorites"

  Scenario: Check plugin integrations
    Given I visit Epidemic Sound
    When I scroll to the integrations section
    Then I should see logos for Adobe and DaVinci Resolve
    And I should see a link to learn more

  Scenario: View pricing plans
    Given I visit Epidemic Sound
    When I click on "Pricing"
    Then I should see options for "Personal" and "Commercial"
    And I should see a comparison of features

  Scenario: Sign up for a free account
    Given I visit Epidemic Sound
    When I click "Create free account"
    And I enter my email and password
    And I submit the form
    Then I should see a confirmation message

  Scenario: Log in to an existing account
    Given I visit Epidemic Sound
    When I click "Log in"
    And I enter valid credentials
    And I submit the login form
    Then I should be redirected to my dashboard

  Scenario: Access help center
    Given I visit Epidemic Sound
    When I scroll to the footer
    And I click "Help center"
    Then I should see support articles
    And I should see a search bar for help topics
