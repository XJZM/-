from selenium.webdriver.common.by import By
from base import BaseAction

class NetworkPage(BaseAction):

    # 第二次封装抽取的
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    # def __init__(self, driver):
    #     self.driver = driver
    def click_more(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

        #第二次封装
        # self.find_element(self.more_button).click()

        # 第三次封装
        self.click(self.more_button)
    def click_mobile_network(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

        # 第二次封装
        # self.find_element(self.mobile_network_button).click()

        # 第三次封装
        self.click(self.mobile_network_button)
    def first_network(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

        # 第二次封装
        # self.find_element(self.first_network_button).click()

        # 第三次封装
        self.click(self.first_network_button)
    def click_2g_network(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

        # 第二次封装
        # self.find_element(self.network_2g_button).click()

        # 第三次封装
        self.click(self.network_2g_button)
    def click_3g_network(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

        # 第二次封装
        # self.find_element(self.network_3g_button).click()

        # 第三次封装
        self.click(self.network_3g_button)



    # 第三次封装后已经把我们自己封装的find_element统一写道base_action这个文件里了
    # # 重新封装系统的find_element
    # def find_element(self, feature):
    #     by = feature[0]
    #     values = feature[1]
    #     return self.driver.find_element(by, values)
    #
