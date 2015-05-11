# Created by xubin at 5/11/15
Feature: Search for whole foods
  # Enter feature description here

  Scenario: Test Basic Search
    Given Open the application
    When Enter Coffee in the search box
    And Click on Search Button
    Then Expected multiple search results to be displayed