import socket
from urllib.parse import urlsplit 

class GetRequest:
    def __init__(self, url, port, headers=[], verbose=False):
        self.url = url
        self.port = port
        self.headers = headers
        self.verbose = verbose
        self.connection = None
    
    def execute_get(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        url_splitted = urlsplit(self.url)
        host = url_splitted.netloc
        path = url_splitted.path
        query = url_splitted.query
        query = "" if not query else "?" + query
        
        request = self.create_request(path, query, host)
        try:
            self.connection.connect((host, self.port))
            result = self.send_request(request)
            self.process_response(result)
        finally:
            self.connection.close()

    def create_request(self, path, query, host):
        request =  "GET " + path + query + " HTTP/1.0\r\nHost: " + host 
        for header in self.headers:
            request += "\r\n" + header
        request += "\r\n\r\n"
        return request

    def send_request(self, request):
        self.connection.sendall(request.encode())
        return self.connection.recv(10000)

    def process_response(self, result):
        response = ""
        while (len(result) > 0):
            response += result.decode("utf-8")
            result = self.connection.recv(10000)
        if (self.verbose) :
            print(response[response.find("\r\n\r\n") + 1:])
        else:
            print(response)