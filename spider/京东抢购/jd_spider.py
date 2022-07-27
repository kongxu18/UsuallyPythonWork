"""
京东软件
"""
from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()
driver.get('https:www.jd.com/')


class JDLOGIN(object):
    def login_jd(self, num, pwd):
        driver.find_element_by_link_text('你好，请登录').click()
        time.sleep(3)
        d = driver.find_element_by_link_text('账户登录').click()
        print(d)
        time.sleep(3)
        driver.find_element_by_id('loginname').send_keys(num)
        driver.find_element_by_id('nloginpwd').send_keys(pwd)
        time.sleep(3)
        driver.find_element_by_id('loginsubmit').click()
        time.sleep(5)
        nowwhandle = driver.current_window_handle
        driver.find_element_by_link_text('我的购物车').click()
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != nowwhandle:
                driver.switch_to_window(handle)  # 切换至窗口 购物车页面
                # time.sleep(5)
                driver.find_element_by_link_text('去结算').click()
                time.sleep(4)

    def start(self, num, pwd, buytime):
        self.login_jd(num, pwd)
        # self.buy_on_time(buytime)


jdlogin = JDLOGIN()
jdlogin.start('手机号', '密码', '秒杀时间')
