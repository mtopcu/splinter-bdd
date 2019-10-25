from splinter.browser import Browser
from behave import *

browser = Browser('chrome')
mySony = 'https://www.sony.co.uk/mysony'


@given('the MySony home page is displayed')
def step_impl(context):
    browser.visit(mySony)


@when('the user click SonyGroup Link')
def step_impl(context):
    browser.find_link_by_text('any of these other online services from the Sony group').click()


@when('I should see "{text}"')
def step_impl(context, text):
    element = browser.is_text_present(text)
    if not element:
        browser.quit()
        assert element, '"%s" term can not be found on the page' % text


@then(u'close the page')
def step_impl(context):
    browser.quit()
