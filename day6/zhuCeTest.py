import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库验证,测试的正常情况
        driver=self.driver
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("zcy003")  # 等于driver.find_element_name("username"),用第一个方法扩展性更好,便于框架封装
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("18600464089")
        driver.find_element(By.NAME, "email").send_keys("2589612@qq.com")
        driver.find_element(By.CLASS_NAME,"reg_btn").click()
        time.sleep(2)
        new_record=DBConnection().execute_sql_command()
        self.assertEqual("zcy003",new_record[1])
        self.assertEqual("2589612@qq.com", new_record[2])
        print(new_record)