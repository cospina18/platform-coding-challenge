Feature: As an API user who wants to query users and bring their information using the get method

  Scenario Outline: The user sends the correct information and the response of the state is validated, the name, age and
  city are as expected.
    Given url urlBase +"/ms_<info>?nombre=<name>&edad=<age>&cuidad=<city>"
    When  method get
    Then status 200
    And match response.name == <messageName>
    And match response.age == <messageAge>
    And match response.city == <messageCity>
    Examples:
      | name   | age | city     | messageName | info | messageAge | messageCity |
      | Juan   | 70  | Medellin | "Juan"      | info | "70"       | "Medellin"  |
      | Andres | 45  | Pasto    | "Andres"    | info | "45"       | "Pasto"     |


  Scenario Outline: the user varies the information in the path to validate the status of the response
    Given url urlBase  +"/ms_<info>?nombre=<name>&edad=<age>&cuidad=<city>"
    When  method get
    Then status <status>
    Examples:
      | name   | age | city     | status | info  |
      | Juan   | 70  | Medellin | 200    | info  |
      | Andres | 45  | Pasto    | 403    | info2 |
      | Juan   | 70  | Medellin | 403    | asdeg |
      | Andres | 45  | Pasto    | 403    |       |

  Scenario Outline:  The user checks the error message that the API responds, sending an error in the name or the age or the city
    Given url urlBase  +"/ms_info?nombre=<name>&edad=<age>&cuidad=<city>"
    When  method get
    Then status 200
    And match response.message == <message>
    Examples:
      | name    | age | city      | message         |
      | Juan2   | 70  | Medellin  | "input invalid" |
      | Andres3 | 45  | Pasto     | "input invalid" |
      | Juan2   | 70a | Medellin  | "input invalid" |
      | Andres3 | 4qw | Pasto     | "input invalid" |
      | Juan2   | 70a | Medellin2 | "input invalid" |
      | Andres3 | 4qw | Pasto1    | "input invalid" |

