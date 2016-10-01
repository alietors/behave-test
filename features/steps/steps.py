from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('we are on "{url}"')
def step_impl(context, url):
    context.browser.get(url)

@when('we search for "{query}"')
def step_impl(context, query):
    search_bar = context.browser.find_element_by_name('q')
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)

@then('we get results')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "resultStats")))

@then('we do not get results')
def step_impl(context):
    WebDriverWait(context.browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="mnr-c"]/div/p[text()[contains(., "did not match")]]')))