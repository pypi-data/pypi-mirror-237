import requests


class vxVaultApi():
    def __init__(self):
        self.apiUrl = "http://vxvault.net/URL_List.php"
    def get_result(self,keyword: str):
        try:
            request = requests.get(self.apiUrl).text.replace("\r","").split('\n')
            if keyword in request:
                response = "malicious"
            else:
                response = "clean"

            return True, None, response
        except Exception as e:
            return False, e, None




