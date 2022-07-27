from selenium import webdriver
import traceback
import time
import re
import io
import sys
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from fake_useragent import UserAgent
import requests


class Spider:
    def __init__(self):
        self.url = 'https://www.xe.com/currencyconverter/'
        self.authorization = 'Basic bG9kZXN0YXI6eDRBZE9MaENEbHQ3TkNLV25sTlhIUXlQTzMzZVo0R00='

    def process_browser_logs_for_network_events(self, logs):
        for entry in logs:
            log = json.loads(entry["message"])["message"]
            if (
                    "Network.response" in log["method"]
                    or "Network.request" in log["method"]
                    or "Network.webSocket" in log["method"]
            ):
                yield log

    def get_authorization(self):
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        prefs = {"profile.managed_default_content_settings.images": 2}

        options.add_experimental_option("prefs", prefs)

        browser = webdriver.Chrome(desired_capabilities=desired_capabilities, options=options)

        errinfo = ''
        authorization = None
        try:
            # print("try")
            browser.get(self.url)
            time.sleep(5)
            logs = browser.get_log("performance")
            events = self.process_browser_logs_for_network_events(logs)

            for item in events:
                if item.get('params') and item.get('params').get('headers'):
                    if item.get('params').get('headers').get('authorization'):
                        authorization = item.get('params').get('headers').get('authorization')
                        if authorization:
                            break
            # print(authorization)
        except Exception as err:
            errinfo = str(err) + "=>" + (traceback.print_exc() if traceback.print_exc() else 'None')
            print(errinfo)
        browser.quit()
        return authorization

    def get_dict(self, authorization):
        headers = {'Authorization': authorization,
                   'User-Agent': UserAgent().random}
        try:
            html_dict = requests.get(
                url='https://www.xe.com/api/protected/midmarket-converter/',
                headers=headers
            ).text
        except Exception as e:
            html_dict = None
        return html_dict

    def get_rate(self, target=None):
        res = self.get_dict(self.authorization)
        if not res:
            self.authorization = self.get_authorization()
            res = self.get_dict(self.authorization)
        print(res)
        return res


if __name__ == '__main__':
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    # argv = sys.argv
    # raise Exception("{};{}".format(len(argv),argv[1]))
    spider = Spider()
    rlt = spider.get_rate()
