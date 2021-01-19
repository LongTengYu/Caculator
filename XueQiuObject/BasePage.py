import yaml
from appium.webdriver.webdriver import WebDriver


class Base_Page():
    black_list = []  # 设置黑名单，主要用于记载意外弹窗控件元素
    error_cont = 0  # 错误计数器
    error_max = 10  # 最大错误值
    params = {}  # 参数字典

    def __init__(self, driver: WebDriver = None): #
        self.driver = driver  # 声明self.driver变量，并获取driver参数

    def find(self, by, locator=None):  # 查找控件函数
        try:
            element = ''  # 声明控件变量
            if isinstance(by, tuple):  # 判断by的数据类型
                element = self.driver.find_element(*by)  # 获取控件方式1
            else:
                element = self.driver.find_element(by, locator)  # 获取控件方式2
            self.error_cont = 0  # 重置错误计数器
            return element  # 返回获取的控件

        except Exception as e:
            self.error_cont += 1  # 当获取元素出现错误时，错误计数器+1
            if self.error_cont > self.error_max:  # 当错误次数大于最大错误值时，直接抛出错误信息
                raise e  # 抛出错误信息
            for black in self.black_list:  # 遍历黑名单
                black_element = self.driver.find_element(*black)  # 获取黑名单控件
                if len(black_element) > 0:  # 判断是否获取到黑名单控件，若获取到了，则执行点击操作，并再次调用find方法
                    black_element.click()  # 执行点击操作
                    return self.find(by, locator)  # 调用find方法
            raise e

    def steps(self, path):  # 用yaml数据驱动方式，操作页面控件   path为yaml文件路径
        with open(path, encoding='utf-8') as f:  # 获取yaml文件路径并规定编码类型
            '''
            yaml数据示例说明：
            - by: xpath   # 指定用何种方式获取控件 
              locator: "//*[@text='行情']"  # 获取控件所用到的属性值  
              action: send  # 指定操作方法
              value: "{value}"  # 向控件输入参数
            '''
            steps: list[dict] = yaml.load(f)  # 获取yaml文件的中的数据
            for step in steps:  # 遍历yaml数据
                if 'by' in step.keys():  # 当step的keys值中等于by，则调用find方法获取页面控件
                    element = self.find(step['by'], step['locator'])  # 获取控件，传入by和locator
                if 'action' in step.keys():  # 判定操作方法
                    if 'click' == step['action']:  # 当操作方法为click时，执行click操作
                        element.click()  # 执行click操作
                    if 'send' == step['action']:  # 当操作方法为send时，执行send_keys，并替换参数同时向控件传入新的参数
                        content: str = step['value']  # 获取step中的参数
                        for param in self.params:  # 遍历参数字典值
                            content = content.replace('{%s}' % param, self.params[param])  # 将step中的参数替换成参数字典值中的数据
                        element.send_keys(content)  # 执行send_keys操作，并向控件传入新参数
