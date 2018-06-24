#selenium执行javascript中的两个关键字：return（返回值）和arguments（参数）
import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost")
driver.implicitly_wait(20)
#点击登录链接
#用javascript的方法找登录链接胡代码：
#用document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码:
#driver.find_element_by_link_text("登录")
#某些元素,用selenium方法找元素比javascript更容易
#虽然selenium不支持removeAttribute的方法
#但是selenium找到登录链接和javascript找到的是同一个元素
#我们可不可以用selenium找到元素.传入到javascript方法里,代替原来的javascript定位
#我们可不可以用selenium找到元素以后,转换成javascript的元素?
#这样以后写javascript就容易很多,不需要childNodes这些方法了
#比如.document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute()
login_link=driver.find_element_by_link_text("登录")
#arguments参数的复数形式,[0]是第一个参数,指的就是js后面的login_link
#所以下面这句代码,相当于把driver.find_element_by_link_text("登录")带入到javascript语句中
#变成了driver.find_element_by_link_text("登录").removeAttribute('target')
#arguments是参数数组,是js字符串后面的所有参数
#一般情况下我们只用到arguments[0],也就是js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#z执行成功的写登录
#返回商城首页
#搜索iphone
#点击商品 用这种方法实现不打开新窗口
#body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a
#复制出来的css往往比较长,我们可以适当的缩写长度
#我们定位元素的目标节点是最后一个节点
#大于号>前面的是父节点,后面的是子节点
#每个节点的第一个单词是标签名,比如a,div,body
#小数点后面表示class属性
#:nth-child(2),nth表示第n个,child表示子节点
#所以:nth-child(2),表示是当前标签是它的父节点的第二个子节点
driver.find_element_by_id("username").send_keys("zcy123")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("进入商城购物")
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品(用这种方法实现不打开新窗口)
#因为img没有target属性,所以要找父节点a
product_link_xpath="/html/body/div[3]/div[2]/div[3]/div/div[1]/a"
dingwei=driver.find_element_by_xpath(product_link_xpath)
driver.execute_script("arguments[0].removeAttribute('target')",dingwei)
dingwei.click()
#在商品详情界面,点击加入购物车
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
#在每个class前面都加一个小数点,并且去掉中间的空格,我们就可以同时用两个属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
#输入收货人等信息(选择地区)
# driver.find_element_by_css_selector("#add-new-address > div:nth-child(1) > input").send_keys("珠珠")
# driver.find_element_by_css_selector("#add-new-address > div:nth-child(2) > input").send_keys("15600158516")
# driver.find_element_by_css_selector("#add-new-area-select > option:nth-child(2)").send_keys("北京市")
driver.find_element_by_name("address[address_name]").send_keys("珠珠")
driver.find_element_by_name("address[mobile]").send_keys("15600158516")

dropdown1=driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素,对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素,专门创建了一个类Select
#dropdown1的类型是一个普通的网页元素
#下面语句的意思,是把一个普通的网页元素,转换成一个下拉框的特殊网页元素

print(type(dropdown1)) #是一个web_element类型,web_element类中只有click和send_keys方法,没有选择下拉框选项的方法
select1=Select(dropdown1)
print(type(select1))#select1是一个select类型
#转换成select类型后,网页元素还是那个元素,但是select类中有选项的方法
select1.select_by_value("220000") #这时,可以通过选项值来定位
time.sleep(2)
select1.select_by_visible_text("吉林省")#也可以通过选项的文本信息定位
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("长春市")
#dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]
#tag_name少用,因为元素太多,所以find_element_by_tag_name不常用,但find_elements_by_tag_name常用
dropdown3=driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("市辖区")
#因为是动态id,所以不能用id定位
#因为class重复,所以不能直接用class定位
#可以用find_elements方法,先找到页面中class=add-new-area-select的元素
#然后在通过下标的方式选择第n个页面元素,类似于javascript方法
driver.find_element_by_css_selector("#add-new-address > div.add-new-specific > input").send_keys("1街2号")
driver.find_element_by_css_selector("#add-new-address > div.add-new-email > input").send_keys("100052")
#点击确定,保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()

