

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url
