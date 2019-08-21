from behave import given, when, then
from behave.log_capture import capture

from site_pom.locators import MainPageLocators

@given("User is on SKF Bearings Homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.open(context.homepage_url)


@when("Click on 'Accept & continue' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if context.driver.find_element(*MainPageLocators.BTN_ACCEPT).is_displayed():
        context.driver.find_element(*MainPageLocators.BTN_ACCEPT).click()


@then("Click on {image_text} image")
def step_impl(context, image_text):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_text(image_text).click()


@then("Click on Select bearing type dropdown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(*MainPageLocators.SELECT_BEARING_TYPE).click()


@then("Verify that {options_list} are displayed")
def step_impl(context, options_list):
    """
    :type context: behave.runner.Context
    :type options_list: str
    """
    opts_list = context.driver.find_elements(*MainPageLocators.OPTIONS_BEARING_TYPE)
    for opt in opts_list:
        assert opt.text in options_list, "This option is not found"

    
@then("Close the dropdown without selecting any option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.move_to_element(MainPageLocators.INPUT_SEARCH_DSGNTN)

