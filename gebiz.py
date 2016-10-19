import unittest
from selenium import webdriver
from scrapy.selector import Selector
import time

class testGebizDriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        # Resize the window to the screen width/height
        self.driver.set_window_size(1600, 1000)

        # Move the window to position x/y
        # self.driver.set_window_position(200, 200)

    def testGebiz(self):
        self.driver.get("https://www.gebiz.gov.sg/ptn/supplier/directory/index.xhtml")

        self.driver.find_element_by_xpath(".//*[@id='contentForm:search']").click()

        time.sleep(2)
        for count in xrange(2, 832):
            self.driver.find_element_by_xpath(
                ".//*[@id='contentForm:j_idt104:j_idt116_Next_" + str(count) + "']").click()
            time.sleep(2)
            self.html = self.driver.page_source
            self.scraping()

        self.driver.quit()

    def scraping(self):
        for i in range(0, 10):
            time.sleep(2)
            try:
                companyName = Selector(text=self.html).xpath(".//*[@class='commandLink_TITLE-BLUE']/text()").extract()
                name = companyName[i].strip() if companyName else ''
                companyPhone = Selector(text=self.html).xpath(
                    ".//*/tbody/tr/td/div/div/span/table/tbody/tr/td[2]/text()").extract()
                phone = companyPhone[i].strip() if companyPhone else ''
                with open('sg-company.txt', 'a') as f:
                    f.write('{0};{1}\n'.format(name,
                                               phone))
            except:
                pass


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()