#Any pytest file should start with test_
#pytest method names should start with test
#Any code should be wrapped in 1 method
#you can mark (tag) tests and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and teardown methodss for test cases -define in conftest file to generalize
#fixture and make it available to all test cases (fixture name into parameters of method)
#datadriven and parametrization can be done with return statements in tuple format
#when you define fixture scope to class only, it will return once before class is initiatedand at the end

import pytest

@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"   #operation
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Test failed Addition do not match"

@pytest.fixture()
def setup():
    print("I will be executed first")

def test_fixureDemo(setup):
    print("I will execute steps in fixtureDemo method")

