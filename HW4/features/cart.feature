Feature: Add product to cart

  Scenario: User adds a product to cart and verifies it's there
    Given I open Target homepage for search
    When I search for "headphones"
    And I add the first product to the cart
    Then I should see the product in the cart
