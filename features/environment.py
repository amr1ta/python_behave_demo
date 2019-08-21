from site_pom.web_factory import get_browser_context


def before_all(context):
    driver = get_browser_context(context.config.userdata['browser'])
    context.driver = driver
    
def after_all(context):
    context.driver.quit()