from urllib3 import requests

class TinetServiceConfig:
    URI_CALL = '/call'


class TinetClient(TinetServiceConfig):
    def __init__(self, tinet_service_url, user_id):
        self.url = tinet_service_url
        self.user_id = user_id

    def __do_post_request(self, uri, data=None):
        return requests.post(uri, data=data, timeout=3)

    '''
    {
        "app_key":"30592b31-857d-4310-9af2-304fc6466784",
        "cno":22334,
        "config":1,
        "phone_number":"17757320683"
    }
    '''
    def auth(self, app_key, ):
        pass

    def call(self, phone_number):
        _payload = {
            'user_id': self.user_id,
            'phone_number': phone_number,
        }
        self.__do_post_request(uri=self.url, data=_payload)

    def rebind(self):
        pass

    def current(self):
        pass
