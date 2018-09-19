from requests import GetRequest

class HttpcClient:
    @staticmethod
    def parse_arguments(args): 
        headers = args.header or []
        verbose = False
        if (args.verbose):
            verbose = True
        data = args.data
        file = args.file
        url = args.URL
        request = args.request

        if (request.lower() == 'get') :
            if (data or file):
                raise ValueError('Flags -f and -d are invalid for GET requests')
            HttpcClient.execute_get_request(url, headers, verbose)
        elif (request.lower() == 'post'):
            if (bool(data) != bool(file)):
                HttpcClient.execute_post_request(url, headers, verbose, data, file)
            else:
                raise ValueError("For POST request, use either -f or -d")
        else:
            raise ValueError('Only GET or POST requests are accepted')
    
    @staticmethod
    def execute_get_request(url, headers, verbose):
        get_request = GetRequest(url, 80, headers, verbose)
        get_request.execute()
    
    @staticmethod
    def execute_post_request(url, headers, verbose, data, file):
        pass