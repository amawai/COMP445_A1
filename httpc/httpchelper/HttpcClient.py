from requests import GetRequest
from requests import PostRequest

class HttpcClient:
    @staticmethod
    def execute_get_request(args):
        url = args.URL
        headers = args.header or []
        verbose = False
        if (args.verbose):
            verbose = True
        get_request = GetRequest(url, 80, headers, verbose)
        get_request.execute()
    
    @staticmethod
    def execute_post_request(args):
        url = args.URL
        headers = args.header or []
        verbose = False
        if (args.verbose):
            verbose = True

        data = args.data
        file = args.file

        if (bool(data) != bool(file)):
            post_request = PostRequest(url, 80, data, file, headers, verbose)
            post_request.execute()
        else:
            raise ValueError("For POST request, use either -f or -d")
        pass
