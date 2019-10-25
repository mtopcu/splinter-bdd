@web
Feature: Go to MySony Web Browsing
  As a QA,
  I want to check click SonyGroup link,
  And check a term on the page


  Scenario: Go to MySony Page on Browser
    Given the MySony home page is displayed
    When the user click SonyGroup Link
    And I should see "Linked accounts for Sony services"
    Then close the page