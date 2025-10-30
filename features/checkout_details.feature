Feature: Checkout details functionality
  As a user
  I want to
  So that

  Background:
    Given I'm authenticated and ready to checkout

    Scenario:
      When I try to proceed without providing a first name
      Then I should see an error about missing first name

    Scenario:
      When I try to proceed without providing a last name
      Then I should see an error about missing last name

    Scenario:
      When I try to proceed without providing a ZIP code
      Then I should see an error about missing ZIP code

    Scenario:
      When I click proceed after providing all required info
      Then I should be redirected to the second checkout page