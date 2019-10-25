@api
Feature: Basic Rest Api Test
  As a QA,
  I want to check data from Rest Api

  Scenario Outline: Check the user name and email
    Given the RestApi url is hit on "<page>" page
    When the response status should be "200"
    Then the first user name should be "<name>"
    Then the first user email should be "<email>"

    Examples:
      | page | name    | email                    |
      | 1    | George  | george.bluth@reqres.in   |
      | 2    | Michael | michael.lawson@reqres.in |
