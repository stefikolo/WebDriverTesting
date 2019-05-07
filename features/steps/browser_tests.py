from behave import *
from sure import expect
from lib.page_objects.homepage import HomePage


use_step_matcher("parse")


@given("I'm opening {website}")
def step_impl(context, website):
    """
    :type context: behave.runner.Context
    :type website: str
    """
    context.driver.get(website)
    homepage = HomePage(context.driver)
    print(homepage.title)



@then("Page title contain {phrase_in_title}")
def step_impl(context, phrase_in_title):
    """
    :type context: behave.runner.Context
    :type phrase_in_title: str
    """
    expect(context.driver.title).to.contain(phrase_in_title)
