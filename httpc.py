import argparse 
from httpc import HttpcClient

def is_key_value_pair(s):
    key_value_pair = s.split(":")
    key_value_pair = [x for x in key_value_pair if x != '']
    if (len(key_value_pair) != 2):
        msg = "Headers must be in this format: key:value"
        raise argparse.ArgumentTypeError(msg)
    return s

def allowed_requests(request):
    if (request.lower() == 'get' or request.lower() == 'post'):
        return request
    else:
        msg = "Accepted requests are GET or POST"
        raise argparse.ArgumentTypeError(msg)

# Arguments to run this file 
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("request", help="Specify GET or POST request", type=allowed_requests)
parser.add_argument("-v", "--verbose", help="verbose",  action="store_true")
parser.add_argument("-h", "--header", help="HTTP headers in key:value format ", action='append', type=is_key_value_pair)
parser.add_argument("-d", "--data", help="Associate body of HTTP request with inline data")
parser.add_argument("-f", "--file", help="Associate body of HTTP request with data from given file ")
parser.add_argument("URL", help="The url determining the targetted HTTP server")
args = parser.parse_args()

httpc_client = HttpcClient()
httpc_client.parse_arguments(args)