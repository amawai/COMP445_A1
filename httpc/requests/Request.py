from abc import ABC, abstractmethod
import re

class Request(ABC):
    def __init__(self, url, port, headers=[], verbose=False):
        self.url = url
        self.port = port
        self.headers = headers
        self.verbose = verbose
        self.connection = None

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
<<<<<<< HEAD
        if (self.verbose) :
=======
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
>>>>>>> 1a4658c2a48b3c0203a1379b0e1bfc98084e490b
            print(response)
        else:
            print(response[response.find("\r\n\r\n") + 1:])

    def process_response_write_in_file(self, result):
        response = ""
        file = open("hello.txt", "w")
        while (len(result) > 0):
            response += result.decode("utf-8")
            result = self.connection.recv(10000)
        if (self.verbose) :
            file.write(response)
            file.close()
            print("the response is written in the file")
        else:
            file.write(response[response.find("\r\n\r\n") + 1:])
            file.close()
            print("the response is written in the file")
