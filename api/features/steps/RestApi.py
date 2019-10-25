import requests
import simplejson as json
from behave import *

url = obj = res = None


@given('the RestApi url is hit on "{num}" page')
def step_impl(context, num):
    global obj
    global res
    r = requests.get("https://reqres.in/api/users?page=" + str(num))
    res = r.status_code
    json_data = r.text
    obj = json.loads(json_data)


@when('the response status should be "{num}"')
def step_impl(context, num):
    assert str(res) == str(num), 'Response should be "%s", not "%s!"' % (str(num), str(res))


@then('the first user name should be "{name}"')
def step_impl(context, name):
    assert name == obj["data"][0]["first_name"], 'Name should be "%s", not "%s"!' % (name, obj["data"][0]["first_name"])


@then('the first user email should be "{email}"')
def step_impl(context, email):
    assert email == obj["data"][0]["email"], 'Email should be "%s", not "%s"!' % (email, obj["data"][0]["email"])
