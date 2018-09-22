import socket
from urllib.parse import urlsplit

class PostRequest:
    def __init__(self, url, port, data, file, headers=[], verbose=False):
        self.url = url
        self.port = port
        self.headers = headers
        self.verbose = verbose
        self.data = data
        self.file = file

    def execute(self):
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
        request = "POST " + path + query + " HTTP/1.0\r\nHost: " + host
        for header in self.headers:
            request += "\r\n" + header
        if self.data is not None:
            for inline_data in self.data:
                request += "\r\n" + inline_data
        elif self.file is not None:
            f = open(self.file, 'r')
            f_data = file.read()
            f.close()
            request += "\r\n" + f_data
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
        if (self.verbose):
            print(response)
        else:
            print(response[response.find("\r\n\r\n") + 1:])
