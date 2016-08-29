from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_observe_skywalker_family(self):
        # Junior padawan has heard about a cool new online Star Wars characters site.
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention Star Wars
        assert 'STAR WARS' in self.browser.title, "Browser title was " + self.browser.title
        self.fail('Finish the test!')

        # and saw Skywalker Family tree with characters picture and descriptions

        # also there was menu with button called Explore

if __name__ == '__main__':
    unittest.main(warnings='ignore')
