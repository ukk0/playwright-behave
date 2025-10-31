Feature: Checkout overview functionality
  As a user on the final checkout overview page
  I want all the details of the purchase be displayed correctly
  So that I can finish my order successfully

  Background:
    Given I'm authenticated and on the final checkout overview

    Scenario: The overview page should contain correct details about the order price
      When I look at the page
      Then The page should contain correct price details

    Scenario: Clicking 'Cancel' should bring user back to the inventory page
      When I click 'Cancel'
      Then I should be redirected to the inventory page

    Scenario: Clicking 'Finish' should successfully finalize the order
      When I click 'Finish'
      Then I should be redirected to the 'Checkout completed' page
