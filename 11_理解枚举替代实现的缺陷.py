"""

关于枚举最经典的例子大概非季节和星期莫属了，它能够以更接近自然语言的方式来表达数据，使得程序的可读性和可维护性大大提高。然而，很不幸，也许你习惯了其他语言中的枚举类型，但在Python3.4以前却并不提供。关于要不要加入枚举类型的问题就引起了不少讨论，在PEP354中曾提出增加枚举的建议，但被拒绝。于是人们充分利用Python的动态性这个特征，想出了枚举的各种替代实现方式。

"""

"""
更多关于flufl.enum的使用可以参考网页http://Pythonhosted.org/flufl.enum/docs/using.html的内容。值得一提的是，Python3.4中根据PEP435的建议终于加入了枚举Enum，其实现主要参考实现flufl.enum，但两者之间还是存在一些差别，如flufl.enum允许枚举继承，而Enum仅在父类没有任何枚举成员的时候才允许继承等，读者可以仔细阅读PEP435了解更多详情。另外，如果要在Python3.4之前的版本中使用枚举Enum，可以安装Enum的向后兼容包enum34，下载地址为https://pypi.Python.org/pypi/enum34。
"""