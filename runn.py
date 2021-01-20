import pytest
import os

if __name__ == '__main__':
    pytest.main(['-v','--alluredir','./temple'])
    os.system('allure generate ./temple -o ./report --clean')