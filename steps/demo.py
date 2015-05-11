from behave import *
from objectRepository.locators import SearchResultsPageLocators
from pages.pages import HomePage

use_step_matcher("re")


@given("Open the application")
def step_impl(context):
    """
    :type context behave.runner.Context
    """


@when("Enter (?P<content>.*) in the search box")
def step_impl(context, content):
    """
    :type context behave.runner.Context
    """
    context.homepage = HomePage(context.driver)
    context.homepage.search_content(content)


@step("Click on Search Button")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    context.resultpage = context.homepage.do_search()


@then("Expected multiple search results to be displayed")
def step_impl(context):
    """
    :type context behave.runner.Context
    """
    assert context.resultpage.is_element_exist(SearchResultsPageLocators.LAB_COFFEE)