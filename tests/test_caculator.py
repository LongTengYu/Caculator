import pytest
import yaml

from src.caculator import Caculator

with open("./testcaculator.yml") as f:
    data = yaml.safe_load(f)
class TestCaculator:
    def setup(self):
        self.cal = Caculator()

    @pytest.mark.parametrize("a,b",data["add"])
    def test_add(self,a,b):
        assert self.cal.add(a,b) == a+b

    @pytest.mark.parametrize("a,b", data["minus"])
    def test_minus(self,a,b):
        assert self.cal.minus(a, b) == a-b

    @pytest.mark.parametrize("a,b", data["multi"])
    def test_multi(self,a,b):
        assert self.cal.multi(a, b) == a*b

    @pytest.mark.parametrize("a,b", data["divide"])
    def test_divide(self,a,b):
        assert self.cal.divide(a, b) == a/b
if __name__=='__main__':
    pytest.main(['test_caculator.py ','-v'])