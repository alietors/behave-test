from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome('webdriver/chromedriver')

def after_all(context):
    context.browser.quit()
