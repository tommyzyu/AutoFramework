# coding = "UTF-8"
# 执行文件
import os
import time
import pytest

if __name__ == "__main__":
    pytest.main()
    time.sleep(5)
    os.system("allure generate ./temp -o ./report --clean")
