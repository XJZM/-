from base import init_driver
from page import Page
class TestSearch:
    def setup(self):
        # 前置代码直接封装成一个函数，返回一个登录手机的信息并且赋值给一个变量，方便调用
        self.driver = init_driver(self)

        # 设置统一入口之前
        # self.display_page = DisplayPage(self.driver)

        # 设置统一入口之后
        self.page = Page(self.driver)
    def test_display_search(self):
        # 没封装之前
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

        # 第一次封装之后
        # self.display_page.click_display()
        # self.display_page.click_search()
        # self.display_page.input_keyword('hello')
        # self.display_page.click_back()

        # 对所有的page文件设置一个统一的入口之后的代码
        self.page.display.click_display()
        self.page.display.click_search()
        self.page.display.input_keyword('hello')
        self.page.display.click_back()
