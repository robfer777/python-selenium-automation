from behave import given, when, then

@given("I open Target homepage")
def step_open_target(context):
    ...

@when("I click the cart icon")
def step_click_cart(context):
    ...

@then('I should see "Your cart is empty" message')
def step_verify_empty_cart(context):
    ...
