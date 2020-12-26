import os

import pytest


class TestCaculator:
    @pytest.mark.run(order=1)
    def test_add(self, get_add_data, get_cal):  # 调用conftest文件的get_add_data和get_cal方法
        assert get_cal.add(get_add_data[0], get_add_data[1]) == get_add_data[2]

    @pytest.mark.run(order=4)
    def test_divide(self, get_divide_data, get_cal):
        assert get_cal.divide(get_divide_data[0], get_divide_data[1]) == get_divide_data[2]

    @pytest.mark.run(order=2)
    def test_minus(self, get_minus_data, get_cal):
        assert get_cal.minus(get_minus_data[0], get_minus_data[1]) == get_minus_data[2]

    @pytest.mark.run(order=3)
    def test_multi(self, get_multi_data, get_cal):
        assert get_cal.multi(get_multi_data[0], get_multi_data[1]) == get_multi_data[2]


if __name__ == '__main__':
    # pytest.main(['test_caculator.py ','-vs'])
    pytest.main(['--alluredir', '../Report', 'test_caculator.py ', '-vs'])  # 生成报表数据
    split = 'allure ' + 'generate ' + '../Report ' + '-o ' + '../Html ' + '--clean'  # 生成Html报告语句
    os.system(split)  # 执行Html生成语句
