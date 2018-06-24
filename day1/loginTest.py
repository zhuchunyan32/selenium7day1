#这个文件用来实现一个登陆功能的自动化操作
#步骤:
#1.打开浏览器
from selenium import webdriver #从谷歌公司一个项目 导入 网络驱动 ,用代码来操作浏览器的
import time
driver = webdriver.Chrome()
#driver = webdriver.Ie()
#设置隐式等待:一旦找到页面元素,马上执行后面的语句
#如果超过20秒,仍然找不到页面元素,那么程序就会报错
driver.implicitly_wait(20)
#2.打开海盗商城网
driver.get("http://localhost/")
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("zcy123")
driver.find_element_by_name("password").send_keys("123456")
#5.点击登录按钮
#所有调用方法,都会提示信息,否则就说明没有该方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功
# time.sleep(10) #Alt+Enter 导包的快捷键,选import this time
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#我们可以通过if语句,判断页面显示的文本和预期的文本是否一致,来判断测试用例是否正常执行
if username_text=='您好 zcy123':
    print("测试执行通过")
else:
    print("测试执行失败")
#因为selenium主要做回归测试,所以测试脚本刚开始都是pass 的,只有开发进行了代码变更,才可能执行失败
#一般工作中不用if ...else 语句做判断,后面再详细讨论这个问题
#time.sleep()这个方法提供了一种固定时间等待
#这里的意义是点击登录按钮后,等待5秒后,再检查用户名是否正常显示
#弊端是,因为网络延迟,并不能确定等待多长时间
#7.点击 进入商城购物 按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()  xpath 可读性差
time.sleep(5)
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页输入搜索条件"iphone"
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
time.sleep(5)
#10.在搜索结果页面,点击第一个商品的图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
#11.点击"加入购物车"
driver.close() #关闭正在打开的窗口
driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)
driver.find_element_by_class_name("goods-add").click()

