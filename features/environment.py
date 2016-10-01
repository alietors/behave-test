from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome('features/webdriver/chromedriver')

def after_all(context):
    context.browser.quit()
