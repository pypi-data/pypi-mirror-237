import re

import requests


class usomApi():
    def __init__(self):
        self.apiUrl = "https://www.usom.gov.tr/url-list.xml"

    def get_result(self, keyword: str):
        try:
            request = requests.get(self.apiUrl).text

            request_filter = re.findall(f"<url>{keyword}</url>", request)

            if len(request_filter) > 0:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None


