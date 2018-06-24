import time
import unittest
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时,这个类不需要再写setup和tearDown方法了,只需要写测试用例方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_name("username").send_keys("zcy123")  # 等于driver.find_element_name("username"),用第一个方法扩展性更好,便于框架封装
        driver.find_element_by_id("password").send_keys("123456")
        old_title=driver.title
        driver.find_element(By.CLASS_NAME, "login_btn").click()
        time.sleep(5)
        new_title=driver.title
        #如果新标题和旧标题不相等,就证明登录成功
        self.assertNotEqual(old_title,new_title)
if __name__ == '__main__':
    unittest.main()