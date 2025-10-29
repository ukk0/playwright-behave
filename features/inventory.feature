Feature: Inventory functionality
  As a user on the inventory page
  I want to see all available inventory and sort products by name and price
  So that I am able to pick the items to add to and remove from my shopping cart

  Background:
    Given I am on the inventory page

    Scenario: Every product listed should include a title, picture, description and a price
      When I look at the page
      Then I should see all products with a title, picture, description and a price

    Scenario: Adding items to the shopping cart is correctly reflected in cart badge
      When I add two items to the cart
      Then I should see two items indicated by the shopping cart badge

    Scenario: Removing items from the shopping cart is correctly reflected in cart badge
      When I remove one of the items from cart
      Then I should see the amount of cart items reduced to one

    Scenario: Products can be reverse-sorted by name
      When I sort the products by 'Name (Z to A)'
      Then The products should be reverse sorted by names

    Scenario: Products can be sorted by name
      When I sort the products by 'Name (A to Z)'
      Then The products should be sorted by names

    Scenario: Products can be sorted by price
      When I sort the products by 'Price (low to high)'
      Then The products should be sorted by prices

    Scenario: Products can be reverse-sorted by price
      When I sort the products by 'Price (high to low)'
      Then The products should be reverse sorted by prices