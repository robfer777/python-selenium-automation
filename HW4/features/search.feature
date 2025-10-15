Feature: Target product search

  Scenario: User can search for a product on Target
    Given I open Target homepage
    When I search for "laptop"
    Then I should see multiple product results
