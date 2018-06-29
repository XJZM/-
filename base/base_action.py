from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():
    def __init__(self, driver):
        self.driver = driver
    # 重新封装系统的click方法
    def click(self, feature):
        self.find_element(feature).click()

    # 重新封装一个输入的方法
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    # 重新封装系统的find_element

    # 第二次修改：因为有的时候电脑或者手机会卡，会导致找元素的时候找不到，那么我们就需要
    # 用到WebDriverWait显示等待，给它一个找元素的时间
    def find_element(self, feature):

        # 加入显示等待之后
        by = feature[0]
        values = feature[1]
        wait = WebDriverWait(self.driver,10,1)
        # x代表形参，x.find_element(by, values对等于return x.find_element(by, values)
        # 那么这个x代表什么呢？代表的是我们最开始拿到的driver,那么它是怎么传到这个匿名函数的呢？
        # 我们举一个例子

        # 传的过程：最开始我们把driver传给了WebDriverWait这个类，那么传一个参数给一个类
        # 就相当于给这个类的初始化方法也就是__init__传一个driver,
        # 初始化方法接收到这个driver之后又把这个driver赋值给了self._driver（就是until）
        # 这个时候就已经把这个driver传给了我们的匿名函数lambda中的x

        # 最后这句话翻译过来就是：我们打开一个应用程序（driver）,然后给它10秒钟，每一秒
        # 找一次我们要找的元素，直到找到并且把它返回。如果没有找到就会报错
        return wait.until(lambda x: x.find_element(by, values))

    # 这个方法等价于匿名函数lambda x: x.find_element(by, values)
    # x代表形参，x.find_element(by, values对等于return x.find_element(by, values
    # def abc(self,x):
    #     by = feature[0]
    #     values = feature[1]
    #     return x.find_element(by, values)


        # 还没有加显示等待之前
        # by = feature[0]
        # values = feature[1]
        # return self.driver.find_element(by, values)


    # 这个是重新对系统的find_elements这个方法进行封装，工具可能现在不会用到，但是不能
    # 保证以后不会用到，所以工具必须准备好
    def find_elements(self, feature):
        by = feature[0]
        values = feature[1]
        wait = WebDriverWait(self.driver, 10, 1)
        return wait.until(lambda x: x.find_elements(by, values))

