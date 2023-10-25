import csv

import requests


class feodoTrackerApi():
    def __init__(self):
        self.apiUrl = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
    def get_result(self,keyword: str):
        try:
            request = csv.reader(requests.get(self.apiUrl).text.splitlines())
            response = "malicious" if any(item[1] == keyword for item in request if len(item) > 1) else "clean"
            return True, None, response
        except Exception as e:
            return False, e, None




