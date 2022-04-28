import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")