from selenium import webdriver
import traceback
import time
import re
import io
import sys
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Spider:
    def __init__(self, target):
        self.target = target
        self.url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From={}&To=CNY'.format(self.target)

    def get_rate(self):

        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        prefs = {"profile.managed_default_content_settings.images": 2}

        options.add_experimental_option("prefs", prefs)

        browser = webdriver.Chrome(desired_capabilities=desired_capabilities, options=options)
        wait = WebDriverWait(browser, 10)
        rate = 0
        updateTime = ''

        errinfo = ''
        try:
            # print("try")
            browser.get(self.url)
            xpath_bds = '//*[@class="result__BigRate-sc-1bsijpp-1 iGrAod"]'
            time_xpath_bds = '//*[@class="result__LiveSubText-sc-1bsijpp-2 iKYXwX"]'
            wait.until(method=EC.presence_of_element_located((By.XPATH, xpath_bds and time_xpath_bds))
                       , message='not find')

            browser.execute_script("window.stop();")

            dd_list = browser.find_elements_by_xpath(xpath_bds)
            if dd_list and len(dd_list[0].text) > 0:
                res = dd_list[0].text
                rate = res.split()[0]

                xpath_bds = '//*[@class="result__LiveSubText-sc-1bsijpp-2 iKYXwX"]'
                timeItem = browser.find_elements_by_xpath(xpath_bds)[0]
                timeMatch = re.search('Last updated (.*UTC)', timeItem.text)
                updateTime = timeMatch.groups(0)[0]

        except Exception as err:
            errinfo = str(err) + "=>" + (traceback.print_exc() if traceback.print_exc() else 'None')
            print(errinfo)
        browser.quit()
        return (rate, updateTime, errinfo)


if __name__ == '__main__':
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # argv = sys.argv

    argv = ['', 'USD']
    # raise Exception("{};{}".format(len(argv),argv[1]))
    spider = Spider(argv[1])
    rlt = spider.get_rate()
    rlt_json = {}
    rlt_json['rate'] = rlt[0]
    rlt_json['time'] = rlt[1]
    rlt_json['err'] = rlt[2]
    print("rlt=" + json.dumps(rlt_json, ensure_ascii=False))
