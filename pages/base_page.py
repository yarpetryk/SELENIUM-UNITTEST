class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
    
    @property
    def is_url(self):
        return self.driver.current_url == self.url