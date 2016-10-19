import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector


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

        # while True:
        # next = self.driver.find_element_by_xpath(".//*[@id='contentForm:j_idt104:j_idt116_" + str(i) + "_" + str(i) + "']")
        self.driver.implicitly_wait(4)
        for count in xrange(2, 10):
            self.driver.find_element_by_xpath(
                ".//*[@id='contentForm:j_idt104:j_idt116_Next_" + str(count) + "']").click()
            self.driver.implicitly_wait(4)
            for i in range(0, 10):
                self.driver.implicitly_wait(10)
                companyName = self.driver.find_element_by_xpath(".//*[@class='commandLink_TITLE-BLUE']")
                name = companyName.text if companyName.text else 'kosong'
                companyPhone = self.driver.find_element_by_xpath(
                    ".//*[@id]/div/table/tbody/tr/td/div/div/span/table/tbody/tr/td[2]")
                phone = companyPhone.text if companyPhone.text else 'kosong'

                with open('sg-company.txt', 'a') as f:
                    f.write('{0};{1}\n'.format(name,
                                               phone))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



