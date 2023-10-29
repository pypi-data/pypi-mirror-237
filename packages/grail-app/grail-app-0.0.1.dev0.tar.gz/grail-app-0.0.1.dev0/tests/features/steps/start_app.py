#  type: ignore

from behave import given, when, then


@given("A app is created")
def flask_setup(context):
    context.app = context.create_app()


@given("I set {name} to {value}")
@when("I set {name} to {value}")
def update_config(context, name, value):
    context.app.config[name] = value


@then("The value of {name} is {value}")
def check_config(context, name, value):
    assert context.app.config[name] == value
