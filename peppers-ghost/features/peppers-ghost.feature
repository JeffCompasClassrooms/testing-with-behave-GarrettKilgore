Feature: Explore the Pepper's Ghost illusion tutorial
  As a curious maker
  I want to explore the tutorial page
  So that I can learn how to build the illusion myself

  Scenario: Load the tutorial page successfully
    Given I open the instructables peppers ghost page
    Then the title should contain "Pepper's Ghost Illusion"
    And the page should contain the text "Step 1: The Basics"
    And the page should contain the text "twall2"
    And I expect that there is at least one picture there
    And the page should contain the text "phantom"

  Scenario: Verify materials listed in the tutorial
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Gaffers Tape"
    And the page should contain the text "C-Stand"
    And the page should contain the text "Lexan"
    And the page should contain the text "White paper"
    And the page should contain the text "Wood Clamp"

  Scenario: Check for key concepts explained
    Given I open the instructables peppers ghost page
    Then the page should contain the text "reflection"
    And the page should contain the text "viewer"
    And the page should contain the text "picture plane"
    And the page should contain the text "transparent"
    And the page should contain the text "illusion"

  Scenario: Confirm presence of instructional steps
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Step 2: Standing Up the Plexi"
    Then the page should contain the text "Step 5: Scene Setup"
    And the page should contain the text "Step 8: Lighting"
    And the page should contain the text "Step 11: Storytelling"
    And the page should contain the text "Step 13: Enjoy"

  Scenario: Validate visual and layout simplicity
    Given I open the instructables peppers ghost page
    Then there should be no element with id "login"
    Then the page should contain the text "Add Comment"
    And there should be no element with name "q"
    And there should be no element with class name "social"
    Then the page should contain the text "Pepper's Ghost Illusion in a Small Space"

  Scenario: Confirm author and engagement metadata
    Given I open the instructables peppers ghost page
    Then the page should contain the text "twall2"
    And the page should contain the text "views"
    And the page should contain the text "comments"
    And the page should contain the text "published"
