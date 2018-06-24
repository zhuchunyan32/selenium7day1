#实现注册功能的文件
from selenium import webdriver #从谷歌公司一个项目 导入 网络驱动 ,用代码来操作浏览器的
driver = webdriver.Chrome()
#2.打开海盗商城网
driver.get("http://localhost/")
#3
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("zcy012")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("18600464083")
driver.find_element_by_name("email").send_keys("18600464083@qq.com")
driver.find_element_by_class_name("reg_btn").click()