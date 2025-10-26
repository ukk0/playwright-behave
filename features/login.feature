Feature: Login functionality
  As a valid user with valid password
  I want to be able to log in successfully
  So that I can access the shopping experience

  Background:
    Given I am on the login page

    Scenario: Successful login with valid credentials
      When I enter valid credentials and click 'Login'
      Then I should be redirected without any errors

    Scenario: Login fails for a locked out user
      When I use a username for locked account and click 'Login'
      Then I should see an error message about locked user

    Scenario: Login fails with missing username
      When I leave the username field empty and click 'Login'
      Then I should see an error message about missing username

    Scenario: Login fails with missing password
      When I leave the password field empty and click 'Login'
      Then I should see an error message about missing password

    Scenario: Login fails with wrong password
      When I enter a valid username and an incorrect password and click 'Login'
      Then I should see an error message about invalid credentials