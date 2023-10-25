import requests

class phishingDatabaseApi():
    def __init__(self, type: str):
        self.type=type
        self.apiUrl_URL = "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-ACTIVE.txt"
        self.apiUrl_IP = "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-IPs-ACTIVE.txt"
        self.apiUrl_DOMAIN = "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-ACTIVE.txt"

    def get_result(self,keyword: str):
        try:
            if self.type == 'url':
                status,error,response =self.url(keyword)

            elif self.type == 'ip':
                status,error,response =self.ip(keyword)

            elif self.type == 'domain':
                status,error,response =self.domain(keyword)

            if not status: raise Exception(error)
            return True, None, response
        except Exception as e:
            return False, e, None



    def url(self,keyword: str):
        try:
            request = requests.get(self.apiUrl_URL).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def ip(self,keyword: str):
        try:
            request = requests.get(self.apiUrl_IP).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def domain(self,keyword: str):
        try:
            request = requests.get(self.apiUrl_DOMAIN).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None
