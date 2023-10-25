import csv

import requests


class tweetFeedApi():
    def __init__(self):
        self.apiUrl = "https://raw.githubusercontent.com/0xDanielLopez/TweetFeed/master/month.csv"
    def get_result(self,keyword: str):
        try:
            request = csv.reader(requests.get(self.apiUrl).text.splitlines())


            for item in request:
                if keyword == item[3]:
                    response = "malicious"
                    break
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None




