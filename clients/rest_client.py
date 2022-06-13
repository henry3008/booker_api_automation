import requests


class RestClient:
    def __init__(self, url):
        self.base_url = url

    def get(self, endpoint, headers=None):
        if headers is None:
            headers = {}
        print("Sending request: ")
        response = requests.request("GET", self.base_url + endpoint, headers=headers)
        self.log_request(response.request)
        print("Response: ")
        self.log_response(response)
        return response

    @staticmethod
    def log_response(response):
        print("Status code: " + str(response.status_code))
        print("Headers: " + str(response.headers))
        print("Body: " + str(response.text))

    @staticmethod
    def log_request(request):
        print("Method: " + str(request.method))
        print("Url: " + str(request.url))
        print("Headers: " + str(request.headers))
        print("Body: " + str(request.body))
