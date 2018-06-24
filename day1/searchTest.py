#1,打开主页
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#2.点击登录按钮
driver.find_element_by_link_text("登录").click()
#3.在搜索框输入iphone

#如果我们向在新的标签页上操作页面元素,怎么办?
#需要切换窗口
#driver.switch_to.window(第二个窗口的名字)
#接下来的问题就是,如果获取第二个窗口的名字了
#selenium提供了浏览器中所有窗口名字的集合
#handle是句柄的意思,把句柄理解为名字就可以了
#driver.window_handles可以理解为一个数组,要求第二个窗口的名字怎么做?
#[1] 表示数组的第二个元素
#所以,第二个窗口的名字是driver.window_handles[1]
#所以,窗口切换的语句就是:
driver.switch_to.window(driver.window_handles[1])
#这时,再试一下,iphone会被输入到哪个搜索框中
driver.find_element_by_name("keyword").send_keys("iphone")

#这就是窗口切换的方法
#[1] 表示第二个元素,[-1]表示最后一个元素
#在python中元祖和列表可以从0开始数,也可以从-1倒着数
#如果这段代码理解了,再回到logintest,点击"加入购物车"
