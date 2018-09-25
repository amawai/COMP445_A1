from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, url, port, headers=[], verbose=False):
        self.url = url
        self.port = port
        self.headers = headers
        self.verbose = verbose
        self.connection = None

    @abstractmethod
    def execute(self):
        return

    def send_request(self, request):
        self.connection.sendall(request.encode())
        return self.connection.recv(10000)

    def process_response(self, result):
        response = ""
        while (len(result) > 0):
            response += result.decode("utf-8")
            result = self.connection.recv(10000)
        if (self.verbose) :
            print(response) 
        else:
            print(response[response.find("\r\n\r\n") + 1:])