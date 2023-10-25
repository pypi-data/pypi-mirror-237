import requests


class phishstatsApi():
    def __init__(self,type: str):
        if type == 'ip':
            self.apiUrl = "https://phishstats.info:2096/api/phishing?_where=(ip,eq,{})"
        else:
            self.apiUrl = "https://phishstats.info:2096/api/phishing?_where=(url,like,{})&_sort=-id"

    def get_result(self,keyword: str):
        try:
            request = requests.get(self.apiUrl.format(keyword)).json()

            if len(request) > 0:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None




