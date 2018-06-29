# 点击base会直接跳转到当前目录的__init__.py文件里，系统的也是一样，
# 所以把导包操作直接写在这个文件里，那么我们导包的时候就不用一级一级的导，
# 而是可以像系统一样直接选择一个文件夹，然后直接选择一个我们想要导入的模块或者类。
# 我的理解：感觉这个跟环境变量有点类似
from base.base_driver import init_driver
# 因为‘.’代表当前文件夹，所以也可以这样写（省略了当前文件夹的名字）
from .base_driver import init_driver
from .base_action import BaseAction