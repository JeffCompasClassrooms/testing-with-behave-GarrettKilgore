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
    Then the page should contain the text "Step 5: In Which We Are Still Making the Plexi Stand Up"
    And the page should contain the text "Step 8: We're Done...or Are We?"
    And the page should contain the text "Step 11: Protecting the Illusion"
    And the page should contain the text "Step 13: Enjoy"

Scenario: Validate visual and layout simplicity
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Instructables"
    And the page should contain the text "Share"
    And the page should contain the text "Follow"
    And the page should contain the text "Comment"
    And the page should contain the text "Favorite"

Scenario: Confirm author and engagement metadata
    Given I open the instructables peppers ghost page
    Then the page should contain the text "twall2"
    And the page should contain the text "Published"
    And the page should contain the text "views"
    And the page should contain the text "comments"
    And the page should contain the text "published"

Scenario: Confirm author and project metadata
    Given I open the instructables peppers ghost page
    Then the page should contain the text "twall2"
    And the page should contain the text "Published"
    And the page should contain the text "views"
    And the page should contain the text "comments"
    And the page should contain the text "Follow"

Scenario: Verify presence of visual setup elements
    Given I open the instructables peppers ghost page
    Then the page should contain the text "mirror"
    And the page should contain the text "plexi"
    And the page should contain the text "projector"
    And the page should contain the text "black cloth"

Scenario: Check for storytelling and performance guidance
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Protecting the Illusion"
    And the page should contain the text "scene"
    And the page should contain the text "viewer"
    And the page should contain the text "phantom"
    And the page should contain the text "illusion"

Scenario: Confirm presence of safety and setup tips
    Given I open the instructables peppers ghost page
    Then the page should contain the text "secure"
    And the page should contain the text "stable"
    And the page should contain the text "angle"
    And the page should contain the text "light"

Scenario: Validate user engagement options
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Comment"
    And the page should contain the text "Favorite"
    And the page should contain the text "Share"
    And the page should contain the text "Follow"

Scenario: Confirm educational terminology and concepts
    Given I open the instructables peppers ghost page
    Then the page should contain the text "Protecting the Illusion"
    And the page should contain the text "scene"
    And the page should contain the text "viewer"
    And the page should contain the text "phantom"
    And the page should contain the text "illusion"

Scenario: Scroll to the illusion setup section
  Given I open the instructables peppers ghost page
  When I scroll to the section containing "Step 5: In Which We Are Still Making the Plexi Stand Up"
  Then the page should contain the text "plexi"
  And the page should contain the text "angle"
  And the page should contain the text "secure"

Scenario: Validate absence of unrelated elements
  Given I open the instructables peppers ghost page
  Then there should be no element with tag name "video"
  And there should be no element with class name "ads-banner"
  And the page should contain the text "illusion"
  And the page should contain the text "viewer"
  And the page should contain the text "phantom"

Scenario: Scroll to and validate final step content
  Given I open the instructables peppers ghost page
  When I scroll to the section containing "Step 13: Enjoy"
  Then the page should contain the text "Enjoy"
  And the page should contain the text "illusion"
  And the page should contain the text "viewer"
  And the page should contain the text "phantom"
