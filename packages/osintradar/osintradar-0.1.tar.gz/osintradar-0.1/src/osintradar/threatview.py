import requests

class threatViewApi():
    def __init__(self, type: str):
        self.type=type
        self.apiUrl_URL = "https://threatview.io/Downloads/URL-High-Confidence-Feed.txt"
        self.apiUrl_IP = "https://threatview.io/Downloads/IP-High-Confidence-Feed.txt"
        self.apiUrl_MD5 = "https://threatview.io/Downloads/MD5-HASH-ALL.txt"
        self.apiUrl_SHA = "https://threatview.io/Downloads/SHA-HASH-FEED.txt"
        self.apiUrl_BTC = "https://threatview.io/Downloads/MALICIOUS-BITCOIN_FEED.txt"
        self.apiUrl_DOMAIN = "https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt"
    def get_result(self,keyword: str):
        try:
            if self.type == 'url':
                status,error,response =self.url(keyword)

            elif self.type == 'ip':
                status, error, response = self.ip(keyword)

            elif self.type == 'md5':
                status, error, response = self.md5(keyword)

            elif self.type == 'sha':
                status, error, response = self.sha(keyword)

            elif self.type == 'btc':
                status, error, response = self.btc(keyword)

            elif self.type == 'domain':
                status, error, response = self.sha(keyword)

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

    def ip(self, keyword: str):
        try:
            request = requests.get(self.apiUrl_IP).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def md5(self, keyword: str):
        try:
            request = requests.get(self.apiUrl_MD5).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def sha(self, keyword: str):
        try:
            request = requests.get(self.apiUrl_SHA).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def btc(self, keyword: str):
        try:
            request = requests.get(self.apiUrl_BTC).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None

    def domain(self, keyword: str):
        try:
            request = requests.get(self.apiUrl_DOMAIN).text.split('\n')

            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None





