Feature: Verify empty cart message

  Scenario: User sees "Your cart is empty" on Target
    Given I open Target homepage
    When I click the cart icon
    Then I should see "Your cart is empty" message
