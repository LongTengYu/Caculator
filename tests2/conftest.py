import pytest
import yaml
import os
from src.caculator import Caculator

yaml_file_path = os.path.dirname(__file__) + "/testcaculator.yml"

# 打开yaml文件，并获取key值对应列表
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']
    minus_data = datas['minus']
    multi_data = datas['multi']
    divide_data = datas['divide']


# 声明fixture，并返回data数据
@pytest.fixture(scope='module', params=add_data)  # scope为作用域  params为参数列表
def get_add_data(request):
    print('开始计算')
    data = request.param  # 获取参数列表中value值
    yield data
    print('计算结束')


@pytest.fixture(scope='module', params=minus_data)
def get_minus_data(request):
    print('开始计算')
    data = request.param
    yield data
    print('计算结束')


@pytest.fixture(scope='module', params=multi_data)
def get_multi_data(request):
    print('开始计算')
    data = request.param
    yield data
    print('计算结束')


@pytest.fixture(scope='module', params=divide_data)
def get_divide_data(request):
    print('开始计算')
    data = request.param
    yield data
    print('计算结束')


@pytest.fixture(scope='class')
def get_cal():
    cal = Caculator()  # 声明Caculator类对象
    return cal  # 返回对象
