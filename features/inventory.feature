Feature: Inventory functionality
  As a user on the inventory page
  I want to see all available inventory and prices
  So that I am able to add to and remove items from my shopping cart

  Background:
    Given I am on the inventory page

    Scenario: Adding items to the shopping cart is correctly reflected
      When I add two item to the cart
      Then I should see two items indicated by tye shopping cart badge