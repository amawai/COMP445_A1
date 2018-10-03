import socket
from urllib.parse import urlsplit
import mimetypes
from .Request import Request

class PostRequest(Request):
    def __init__(self, url, port, data, file, headers=[], verbose=False):
        super().__init__(url, port, headers, verbose)
        self.data = data
        self.file = file

    def execute(self, redirected=0):
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
            redirection = self.process_response(result)
            if (redirection):
                if (redirected < 5):
                    self.execute(redirected + 1)
                else:
                    print("Too many redirections, operation aborted")
        finally:
            self.connection.close()

    def create_request(self, path, query, host):
        request = "POST " + path + query + " HTTP/1.0\r\nHost: " + host
        for header in self.headers:
            request += "\r\n" + header
        if self.data is not None:
            request += "\r\nContent-Length: " + str(len(self.data))
            request += "\r\n\r\n" + self.data
        elif self.file is not None:
            f = open(self.file, 'r')
            f_data = f.read()
            f.close()
            request += "\r\nContent-Type:" + mimetypes.guess_type(self.file)[0] or "application/json"
            request += "\r\nContent-Length: " + str(len(f_data))
            request += "\r\n\r\n" + f_data
        request += "\r\n\r\n"
        return request
