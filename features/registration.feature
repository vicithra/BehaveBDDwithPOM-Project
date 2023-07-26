Feature: Registration Feature
  Scenario Outline: Validating the registration feature
    Given I navigate to qa.way2automation.com
    When I enter the name as "<name>"
    Then I enter the phone number as "<phonenumber>"
    And I enter the mailID as "<email>"
    And I select the city as "<city>"
    And I enter the country as "<country>"
    And I enter the username as "<username>"
    And I enter the password as "<password>"
    And I click the submit button
    Examples:
      | name        | phonenumber | email                     | country | city   | username     | password |
      | Rameshwaran | 9711911558   | ramwaran@gmail.com        | Germany | Berlin | ram1990      | werwerwer|
       |Vicithra | 9999911558   | vicithramurugan@gmail.com        | Australia | Melbourne | vici1995      | adfadfgasdg|