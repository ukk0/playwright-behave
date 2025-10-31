Feature: Checkout details functionality
  As a user on the checkout page to provide customer details
  I want the form to validate my inputs correctly
  So that I can successfully provide my info and proceed with my purchase

  Background:
    Given I'm authenticated and ready to checkout

    Scenario: Form cannot be submitted without providing a first name
      When I try to proceed without providing a first name
      Then I should see an error about missing first name

    Scenario: Form cannot be submitted without providing a last name
      When I try to proceed without providing a last name
      Then I should see an error about missing last name

    Scenario: Form cannot be submitted without providing a ZIP code
      When I try to proceed without providing a ZIP code
      Then I should see an error about missing ZIP code

    Scenario: Form can be successfully submitted with all info provided
      When I click proceed after providing all required info
      Then I should be redirected to the second checkout page