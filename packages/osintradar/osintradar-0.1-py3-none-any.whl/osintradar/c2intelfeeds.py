import csv

import requests


class c2intelFeedsApi():
    def __init__(self, type):
        if type == 'ip':
            self.apiUrl = "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/IPC2s-30day.csv"
        else:
            self.apiUrl = "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/domainC2s-30day.csv"


    def get_result(self,keyword: str):
        try:
            request = csv.reader(requests.get(self.apiUrl).text.splitlines())
            response = "malicious" if any(item[0] == keyword for item in request if len(item) > 1) else "clean"
            return True, None, response
        except Exception as e:
            return False, e, None
