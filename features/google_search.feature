Feature: Testing google

  Scenario: Google search works
    Given we are on "http://www.google.com"
    When we search for "cats"
    Then we get results

  Scenario: Google search do not works
    Given we are on "http://www.google.com"
    When we search for "jksadhAYSDGKAhd,AHDGAKHDgaHDKd"
    Then we do not get results