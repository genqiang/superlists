from selenium import webdriver
import unittest

# inherit from unittest.TestCase
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # method start with test_ is a test case!!!
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

#assert 'To-Do' in browser.title, "Browser title was " + browser.title

# She is invited to enter a to-do item straight away

#She types "Buy peacock feathers" into a text box

# When she hits enter, the page updates, and now the page lists

# 1. Buy peacock feathers" as an item in a to-do list

# There is still a test box inviting her to add another item. SHe enters "Use peacock feathers to make a fly"

# The page updates again, and now show both items on her list

# the site remembers the list

#browser.quit()