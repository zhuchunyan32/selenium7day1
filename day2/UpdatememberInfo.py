#1.登录海盗商城
#因为大部分测试用例都会用到登录功能,那么我们可不可以把登录功能单独封装成一个方法,每次直接调用这个方法就可以
#这样,以后每次登录,直接调用方法
from selenium import webdriver
import time
#文件名,类名,包名,变量名都以字母开头,可以有数字和下划线,不能有空格和中文
from day2.loginTest import Login
driver=webdriver.Chrome()
#每次创建浏览器时,implicitly_wait固定写一次,对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要检测页面的加载时间,什么时候页面加载完,什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存,pycharm会自动释放内存
#代码运行完,检测到Login()对象不再被使用,系统会自动释放内存
#让登录方法和下面的点击账号设置用同一个浏览器
#我们已经创建一个空白浏览器,后续的所有操作都应该在这个浏览器上执行
Login().loginWithDefaultUser(driver)
#2.点击"账号设置"
#本来点击"账号设置",需要使用driver这个变量,但是文件中没有driver了,怎么办?
#可以重新声明一个driver么?
driver.find_element_by_link_text("账号设置").click()
#3.点击"个人资料"
driver.find_element_by_link_text("个人资料").click()
#patial_link_text可以使用链接的一部分进行元素定位
#当链接文本过长时,推荐使用patial_link_text
#使用patial_link_text方法时,可以用链接中的任意一部分,只要在网页中唯一即可
#xpath的方法比较通用,可以用工具自动生成
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改真实姓名
#如果输入框中原本有内容,那么修改内容时,先清空原来的值,用clear()方法
#实际上,一个良好的编程习惯是在每次send_keys前,先做clear()操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("朱春燕")
#5.修改性别
#保密,男,女的唯一区别是value属性值不同
#可以通过value属性来定位?
#实际上可以通过任何属性来定位
#要想通过value属性定位有两种方法:Xpath和css
#通过cssselect定位元素,只需要在唯一属性的两边加一对中括号就可
# driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中,//表示采用相对路径定位元素
#相对路径一般通过元素的特殊属性查找元素
#/单斜杠表示绝对路径,一般都是从/html开始定位元素
#绝对路径一般通过元素的位置,层级关系查找元素,当页面布局发生变化时,受到的影响比较大
#相对路径,查询速度慢,需要遍历更多的节点
#工作中推荐用css_selector,查询速度比xpath快一点
#xpath在某些浏览器支持不太好
#css_selector所有前端开发都会用
#*星号表示任意节点
#[@]表示任意属性
# driver.find_element_by_xpath('//*[@value="2"]').click()
#javascript的getElementsByClassName()方法可以找到页面上的符合条件的所有元素
#然后下标取其中的第n个元素,也可以定位
#selenium也可以吗?可以
#要找页面上符合条件的唯一元素就用find_elements方法
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
#一下一下点年月日是可以实现的,但是稳定性比较差,并且很难修改日期
#我们右键检查,发现日历控件是一个文本输入框
#那可以用send_keys()方法吗?不可以
#因为属性readonly是只读,写个javasvript删除此属性

driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys('1952-02-02')

#7.修改qq
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("254645")
#8.点击确定,保存成功

driver.find_element_by_id("qq").submit()
time.sleep(10)
driver.switch_to.alert.accept()