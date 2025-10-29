Feature: Navigation functionality
  As a user
  I want to be able to open and close the side menu
  So that I can use the menu for navigation

  Background:
    Given I'm authenticated and on the inventory page

    Scenario: Side navigation menu can be opened and closed
      When I open the side navigation menu
      Then I can close the menu

    Scenario: User can navigate to inventory page from side navigation menu
      When I navigate to the shopping cart page
      And I open the side navigation menu
      And I choose the option 'All Items'
      Then I should be redirected to the inventory page

    Scenario: User can navigate to 'About' page from side navigation menu
      When I open the side navigation menu
      And I choose the option 'About'
      Then I should be redirected to the SauceLabs 'About' page

    Scenario: User can logout from side navigation menu
      When I open the side navigation menu
      And I choose the option 'Logout'
      Then I should be redirected to the login page
