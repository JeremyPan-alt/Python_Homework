from DrissionPage import ChromiumPage
import time


page = ChromiumPage()
page.get('https://jwpd.jsei.edu.cn/xtgl/index_initMenu.html?jsdm=&_t=1719974642340')

# 通过备用入口直接登录教务系统
if page.ele('tag:title').value == '教学管理信息服务平台':
    username = page.ele('#yhm')
    username.input('230812')
    password = page.ele('#mm')
    password.input('1997522@pan')
    login = page.ele('#dl')
    login.click()

# 选择下拉菜单，进入成绩录入界面
# 成绩录入栏的几个按钮id相同，需要执行链式查找
# 成绩按钮为nav栏下ul里的第三个li标签
grade_btn = page.ele('#cdNav').child('tag:ul').children()[2]
grade_btn.click()
register_btn = grade_btn.ele('tag:ul').child('tag:li').child('tag:a')
register_btn.click()

# 等待已阅读按钮走时
page.get('https://jwpd.jsei.edu.cn/cjlrgl/jscjlr_cxJscjlrIndex.html?doType=details&gnmkdm=N302505&layout=default')
time.sleep(8)
btn_OK = page.ele('#btn_yd')
btn_OK.click()

time.sleep(5)
