from requests import GetRequest

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
            print('Sending post request')
        else:
            raise ValueError("For POST request, use either -f or -d")
        pass