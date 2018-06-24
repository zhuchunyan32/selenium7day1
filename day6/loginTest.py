from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

# 3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("zcy123")
driver.find_element_by_name("password").send_keys("123456")
# 5.点击登录按钮
# 所有调用方法,都会提示信息,否则就说明没有该方法
driver.find_element_by_class_name("login_btn").click()

#点击商城购物会报错,因为中间有个登录成功页面,所以不能直接到达该链接
#解决办法有三个:隐式等待,time.sleep(),显示等待
#显示等待代码:


# WebDriverWait(driver,20,0.5).until(expected_conditions)
WebDriverWait(driver,20,0.5).until(EC.visibility_of_element_located((By.LINK_TEXT,"进入商城购物")))#这句话显示等待的代码和time.sleep(20)作用一样

driver.find_element_by_link_text("进入商城购物").click()
