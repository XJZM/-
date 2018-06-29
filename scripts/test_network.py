from base import init_driver
from page import Page
class TestNetwork:
    def setup(self):
        # 1.前置代码直接封装成一个函数，返回一个登录手机的信息并且赋值给一个变量，方便调用
        self.driver = init_driver(self)
        # 2.然后再把这个self.driver作为实参传进这个NetworkPage(self.driver)类里
        # 而一个类被创建对象的时候会自动调用__init__()这个方法，那么就相当于把传进类里
        # 的参数自动的传进__init__()这个方法。这就是初始化
        # self.network_page=NetworkPage(self.driver)

        # 统一入口之后的，我们就不用每个页面都去创建一个对象了，只要给那个入口单独创建一个对象
        # 我们需要用的时候，就直接调用这个入口里面的某某页面就好了（因为入口文件我们都封装好了别的页面的）
        self.page = Page(self.driver)
    def test_network_2g(self):
        # 没封装之前
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

        # 第一次封装之后
        # self.network_page.click_more()
        # self.network_page.click_mobile_network()
        # self.network_page.first_network()
        # self.network_page.click_2g_network()

        # 对所有的page文件设置一个统一的入口之后的代码
        # 为什么这里的network（其余的一样）是一个方法，调用的时候可以不用写括号呢?详细解释看page页面
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.first_network()
        self.page.network.click_2g_network()

    def test_network_3g(self):
        # 没封装之前
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

        # 第一次封装之后
        # self.network_page.click_more()
        # self.network_page.click_mobile_network()
        # self.network_page.first_network()
        # self.network_page.click_3g_network()

        # 对所有的page文件设置一个统一的入口之后的代码
        self.page.network.click_more()
        self.page.network.click_mobile_network()
        self.page.network.first_network()
        self.page.network.click_3g_network()

