# 分析：
    # 以后脚本的页面可能不只是用到display_page的方法，也有可能是network_page中的方法
    # 也有可能是别的页面的方法，那么我们就需要给这些页面统一一个入口，然后我们调用的时候就选择
    # 我们要调用的那个页面的方法
    # 好处：
        # 对于多页面，可以少些很多代码
from page import DisplayPage
from page import NetworkPage
from base import BaseAction
class Page(BaseAction):
    # def __init__(self,driver):
    #     self.driver = driver
    # property是一个修饰符，作用是可以让一个方法变成一个变量，这样我们调用的时候就不需要写括号了，阅读起来更舒适
    @property
    def display(self):
        return DisplayPage(self.driver)
    @property
    def network(self):
        return NetworkPage(self.driver)