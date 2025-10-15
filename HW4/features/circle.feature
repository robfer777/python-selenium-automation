Feature: Verify Target Circle benefits
  Scenario: User sees at least 10 benefit cells on Circle page
    Given I open Target Circle page
    Then I should see at least 10 benefit cells
