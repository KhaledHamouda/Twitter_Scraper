import unittest
import main
from selenium import webdriver

'''
    Unit testing for the low level function function..
'''

class Test_Twitter_Scraper(unittest.TestCase):
    account = ["https://twitter.com/Mr_Derivatives", "https://twitter.com/RoyLMattox"]
    ticker = '$TSLA'
    driver = webdriver.Chrome()
    intervalTime=2

    def test_scraping_profile(self):
        #Scraping a single account.
        self.assertEqual(main.account_web_scraper(self.account[0],self.ticker,self.driver), [2, "@Mr_Derivatives"])
        self.assertTrue(main.account_web_scraper(self.account[1],self.ticker,self.driver),[0,'@RoyLMattox'])


if __name__ == '__main__':
    unittest.main()
