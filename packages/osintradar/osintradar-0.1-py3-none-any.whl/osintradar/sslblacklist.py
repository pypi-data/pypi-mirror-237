import csv

import requests


class sslBlackListApi():
    def __init__(self):
        self.apiUrl = "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv"
    def get_result(self,keyword: str):
        try:
            request = csv.reader(requests.get(self.apiUrl).text.splitlines())
            response = "malicious" if any(item[1] == keyword for item in request if len(item) > 1) else "clean"
            return True, None, response
        except Exception as e:
            return False, e, None
