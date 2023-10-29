from getpass import getpass
from chainge.config import CHAINGE_API_KEY, CHAINGE_API_ENDPOINT

import requests

class ChaingeAPI(requests.Session):

    def __init__(self, api_key = None, api_endpoint = CHAINGE_API_ENDPOINT): 

        #Load in the API key
        if api_key:
            self.api_key = api_key
        elif CHAINGE_API_KEY:
            self.api_key = CHAINGE_API_KEY
        else:
            self.api_key = getpass("Enter your Chainge API key").strip()

        if not self.api_key:
            raise Exception("We weren't able to properly retrieve your API Key")

        #Do any additional startup work 
        self.api_endpoint = api_endpoint

    #Generalized machinery methods for request operations
    def request(self, method, url, *args, **kwargs):
            joined_url = urljoin(self._base_url, url)
            if self._authorization:
                headers = {
                    **kwargs.get("headers", {}),
                    headers: {
                        'X-RapidAPI-Key': self.api_key,
                        'X-RapidAPI-Host': self.api_endpoint 
                    }
                }
            else:
                headers = kwargs.get("headers", {})

            return super().request(method, joined_url, *args, **kwargs, headers=headers)
        

chainge_api = ChaingeAPI()

#Decoupling logic -- generalize the adapter, since most of the heavywork is going to be related to making 
# get requests to a specific endpoint
class StockAdapter:
    '''
        Adapter for all stock related Langchain tooling
    '''
    
    def __init__(self, chainge_api: ChaingeAPI):
        self.chainge_api = chainge_api
    
    def lookup(self, keyword):
        '''
            Given a single keyword, returns a set of potential stock tickers

            apple --> [AAPL, AAPP, etc]
        '''
        out = self.chainge_api.get(f'stock/lookup/{keyword}').json()
        print(out)
        return out

stock_api = StockAdapter(chainge_api = chainge_api)