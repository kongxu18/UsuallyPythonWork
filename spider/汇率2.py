import requests
import json
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
import traceback


class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://www.xe.com/api/protected/midmarket-converter/'

    def process_browser_logs_for_network_events(self, logs):
        for entry in logs:
            log = json.loads(entry["message"])["message"]
            if (
                    "Network.response" in log["method"]
                    or "Network.request" in log["method"]
                    or "Network.webSocket" in log["method"]
            ):
                yield log

    def get_Authorization(self):
        authorization = ''
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(desired_capabilities=desired_capabilities, options=options)
        try:
            browser.get(self.url)
            time.sleep(5)
            logs = browser.get_log("performance")
            # events = self.process_browser_logs_for_network_events(logs)
            for i in logs:
                print(i)





        except Exception as err:
            errinfo = str(err) + "=>" + (traceback.print_exc() if traceback.print_exc() else 'None')
            print(errinfo)
        browser.quit()
        return authorization

    def run(self):
        res_dict = self.get_dict()
        self.get_Authorization()


    def get_dict(self):
        headers = {'Authorization': 'Basic bG9kZXN0YXI6eDRBZE9MaENEbHQ3TkNLV25sTlhIUXlQTzMzZVo0R00=',
                   'User-Agent': UserAgent().random}
        try:
            html = requests.get(
                url=self.url,
                headers=headers
            ).text
        except Exception as e:
            html = 'error:failed get rate'
        return html


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
