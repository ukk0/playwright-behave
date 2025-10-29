Feature: Shopping cart functionality
  As a user on the shopping cart page
  I want to
  So that I can

  Background:
    Given I'm authenticated and in pre-filled shopping cart page

    Scenario: User can leave the shopping cart via 'Continue shopping'
      When I click the button 'Continue shopping'
      Then I should be redirected back to the shop

    Scenario: User can move to checkout from the shopping cart
      When I click the button 'Checkout'
      Then I should be redirected to first step of the checkout

    Scenario: Items can be removed from shopping cart one by one
      When I click 'Remove' on a cart item
      Then The item should be removed and the amount of items in cart reduced
