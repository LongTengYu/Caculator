import pytest

from Appium.XueQiuObject.app import App


class TestSearch():
    def test_s(self):
        a = App()  # 声明App类对象
        a.start()  # 调用start方法
        '''
        因从main方法开始，每个方法都调用并返回下一级页面类。所以依次调用每个页面并通过yaml数据驱动的方式对其进行操作
        '''
        a.main().goto_market().goto_search().search('jd')


if __name__ == '__main__':
    pytest.main(['test_search.py', '-vs'])  # 执行测试
