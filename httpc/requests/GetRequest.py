import socket
from urllib.parse import urlsplit 
from .Request import Request

class GetRequest(Request):
    def __init__(self, url, port, headers=[], verbose=False):
        super().__init__(url, port, headers, verbose)
    
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
        request =  "GET " + path + query + " HTTP/1.0\r\nHost: " + host 
        for header in self.headers:
            request += "\r\n" + header
        request += "\r\n\r\n"
        return request