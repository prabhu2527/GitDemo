#Any pytest file should start with test_
#pytest method names should start with test
#Any code should be wrapped in 1 method
#method name should have sense
# -k stands method name execution
# -s console log in output, -v stands for more info metadata
#you can run specific file with py.test <filename>
import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_GreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])


