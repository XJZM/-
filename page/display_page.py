from selenium.webdriver.common.by import By
from base import BaseAction
class DisplayPage(BaseAction):
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    # 当创建一个类DisplayPage()对象时会自动调用__init__方法，所以在DisplayPage()
    # 中传的参数就等同于给__init__方法传参数
    # 把DisplayPage(self.driver)中的self.driver
    # （这里面的self.driver=init_driver(self)）传给__init__(self,driver)
    # 中的driver,然后driver再把这个数据赋值给self.driver,然后每次调用就可以
    # 不用每个方法都传一个参数，而可以直接调用

    # 因为本页面的这个类DisplayPage继承了父类BaseAction，所以子类可以不用初始化传入driver
    # def __init__(self,driver):
    #     self.driver = driver

    def click_display(self):
        # 第一次封装
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()

        # 第二次封装：重新对find_element这个方法进行封装，自己定义一个，不用系统给的。
        # 并且把方法里面的两个参数放在一个元组里，这样我们调用的时候只需要把元组传进去，
        # 而且涉及到需要改查找元素方式的时候只需要改元组里面的内容，这样子可维护性和可扩展性就会更强

        # 下面这句话的意思就是：我们自己封装的find_element这个函数去找一个叫display_button的元素（最开始定义好了），
        # 而我们自己封装的这个find_element，封装的内容就是是调用系统的find_element去找一个元素
        # 然后把怎么找这个元素，用什么找直接作为参数传入系统的find_element，然后在返回给我们自己
        # 定义的find_element，最后再去click

        # 那么我们的需求就是：我们自己重新封装一个click，让我们自己的click去找这个元素
        # 这样的话，我们就可以调用自己封装的click，它实际上已经帮我们找到了这个元素
        # 首先，我们要新建一个click函数
        # self.find_element(self.display_button).click()

        # 第三次封装
        self.click(self.display_button)
    def click_search(self):
        # 第一次封装
        # self.driver.find_element_by_id("com.android.settings:id/search").click()

        # 第二次封装
        # self.find_element(self.search_button).click()

        # 第三次封装
        self.click(self.search_button)
    def input_keyword(self,content):
        # 第一次封装
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")

        # 第二次封装
        # self.find_element(self.search_edit_text).send_keys(content)

        # 第三次封装
        self.input(self.search_edit_text, content)
    def click_back(self):
        # 第一次封装
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

        # 第二次封装
        # self.find_element(self.back_button).click()

        # 第三次封装
        self.click(self.back_button)

    # 我们把对系统重新定义的方法统一放到一个文件里（base_action），因为这些方法我们是经常用的，
    # 只要继承那个工具类（base_action），我们就可以调用这些方法，也就是说可以直接使用这个工具

    # 那么问题来了，把这些方法直接放到另外一个文件里，又要怎么拿到driver呢？也就是我们的登录
    # 手机那个前置代码。 这个时候可以这样解决： 和Display_Page这个类一样，我们先去初始化
    # 一个__init__方法，把driver传给它。
    # 这个时候问题又来了，这个页面的__init__也报错了，为什么呢？ 因为你只能传入一个driver
    # 写了两个初始化方法，系统不知道你要用哪个类的初始化数据
    # （因为Display_Page这个类继承了我们的工具类BasePage,所以就会有两个__init__）
    # 解决的方法有2个：
        # 第一个就是，继承的这个文件（Display_Page）直接不写初始化方法，父类（BasePage）去初始化把driver传进去就好了。那么就不会传2次driver了
        # 第二个就是，父类的写了初始化，子类的也写初始化，但是子类的初始化必须调用父类的初始化

    # # 重新封装系统的click方法
    # def click(self, feature):
    #     self.find_element(feature).click()
    #
    # #重新封装一个输入的方法
    # def input(self, feature, text):
    #     self.find_element(feature).send_keys(text)
    #
    # # 重新封装系统的find_element
    # def find_element(self, feature):
    #     by = feature[0]
    #     values = feature[1]
    #     return self.driver.find_element(by, values)