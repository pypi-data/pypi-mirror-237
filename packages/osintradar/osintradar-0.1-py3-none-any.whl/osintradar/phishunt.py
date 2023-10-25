import requests


class phishuntApi():
    def __init__(self):
        self.apiUrl = "https://phishunt.io/feed.txt"
    def get_result(self,keyword: str):
        try:
            request = requests.get(self.apiUrl).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None




