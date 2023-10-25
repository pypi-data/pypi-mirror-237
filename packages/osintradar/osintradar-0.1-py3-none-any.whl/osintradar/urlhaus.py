import requests

class urlHausApi():
    def __init__(self):
        self.apiUrl = "https://urlhaus.abuse.ch/downloads/text_recent/"
    def get_result(self,keyword: str):
        try:
            request = requests.get(self.apiUrl).text.splitlines()

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None




