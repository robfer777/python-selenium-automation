Feature: Practice Selenium Waits and Loop for product colors

  Scenario: Verify product colors on Target page
    Given I open Target product page
    When I click through each color option
    Then each color should be selected successfully