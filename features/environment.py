from site_pom.web_factory import get_browser_context


def before_all(context):
    driver = get_browser_context(context.config.userdata['browser'])
    context.driver = driver
    context.homepage_url = context.config.userdata['homepage_url']
    
def after_all(context):
    context.driver.quit()