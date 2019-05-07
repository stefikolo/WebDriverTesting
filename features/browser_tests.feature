# Created by majowm01 at 2019-04-05
Feature: I want to test usage of drivers through tags and special setup created in environment file

  @firefox
  Scenario Outline: open python website in ff
    Given   I'm opening <website>
    Then    Page title contain <phrase_in_title>


    Examples:
      | website            | phrase_in_title |
      | https://demoqa.com | ToolsQA         |

  @chrome
  Scenario Outline: open python website in chrome
    Given   I'm opening <website>
    Then    Page title contain <phrase_in_title>


    Examples:
      | website               | phrase_in_title |
      | http://www.python.org | Python          |