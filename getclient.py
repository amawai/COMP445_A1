import argparse 
import socket
from urllib.parse import urlsplit

#NOTE: THIS FILE SERVES AS AN EXAMPLE FOR HOW A GET REQUEST COULD BE IMPLEMENTED

def run_client(url, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url_splitted = urlsplit(url)
    host = url_splitted.netloc
    path = url_splitted.path
    query = url_splitted.query
    request = "GET " + path + query + " HTTP/1.0\r\nHost: " + host + "\r\n\r\n"
    request_in_bytes = request.encode()
    try:
        conn.connect((host, port))
        conn.sendall(request_in_bytes)
        result = conn.recv(10000)
        while (len(result) > 0):
            print(result.decode("utf-8"))
            result = conn.recv(10000)   
    finally:
        conn.close()

# Arguments to run this file 
parser = argparse.ArgumentParser()
parser.add_argument("request", help="Specify GET or POST request", default="get")
parser.add_argument("-v", "--verbose", help="verbose",  action="store_true")   
parser.add_argument("URL", help="The url determining the targetted HTTP server", default="httpbin.org")
args = parser.parse_args()
if (args.verbose):
    print("Verbosity has been activated but doesn't do anything yet\n")

##Run using  python3 getclient.py get http://httpbin.org/status/418
run_client(args.URL, 80)