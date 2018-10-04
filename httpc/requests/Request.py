from abc import ABC, abstractmethod
import re

class Request(ABC):
    def __init__(self, url, port, writefile, headers=[], verbose=False):
        self.url = url
        self.port = port
        self.headers = headers
        self.verbose = verbose
        self.connection = None
        self.writefile = writefile

    @abstractmethod
    def execute(self, redirected=0):
        pass

    def send_request(self, request):
        self.connection.sendall(request.encode())
        return self.connection.recv(10000)

    def process_response(self, result):
        response = ""
        while (len(result) > 0):
            response += result.decode("utf-8")
            result = self.connection.recv(10000)
        status_code = re.findall(r"(?<=HTTP\/\d\.\d )(\d\d\d)", response)
        if (len(status_code) >= 1):
            status_code = int(status_code[0])
        if (status_code == 302):
            self.redirect(response)
            return True
        else:
            self.display_response(response)
            return False

    def redirect(self, response):
        location = re.findall(r"(?<=Location\: )(.*)", response)
        if (len(location) > 0):
            location_str = str(location[0]).replace("\r", "")
            self.url = location_str
        else:
            print("Failed to find new url location")

    def display_response(self, response):
        if (self.verbose):
            if self.writefile is not None:
                f = open(self.writefile, "w")
                f.write(response)
                f.close()
                print("the response is in the file")
            else:
                print(response)
        else:
            if self.writefile is not None:
                f = open(self.writefile, "w")
                f.write(response[response.find("\r\n\r\n") + 1:])
                f.close()
                print("the response is in the file")
            else:
                print(response[response.find("\r\n\r\n") + 1:])

    
