import pytest

from PythoSelenium.pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self,dataLoad):
        log=self.test_getLogger
        print(dataLoad)
        log.info(dataLoad[0])
        print(dataLoad[0])

        print(dataLoad[2])
        log.info(dataLoad[2])