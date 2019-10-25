import requests
import simplejson as json
from behave import *


class User:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.status = ""


user = User()


@given('the RestApi url is hit on "{num}" page')
def step_impl(context, num):
    r = requests.get("https://reqres.in/api/users?page=" + str(num))
    user.status = r.status_code
    obj = json.loads(r.text)  # Text response is being converted to Json format.
    user.name = obj["data"][0]["first_name"]
    user.email = obj["data"][0]["email"]


@when('the response status should be "{num}"')
def step_impl(context, num):
    assert str(user.status) == str(num), 'Response should be "%s", not "%s"!' % (str(num), str(user.status))


@then('the first user name should be "{name}"')
def step_impl(context, name):
    assert name == user.name, 'Name should be "%s", not "%s"!' % (name, user.name)


@then('the first user email should be "{email}"')
def step_impl(context, email):
    assert email == user.email, 'Email should be "%s", not "%s"!' % (email, user.email)
