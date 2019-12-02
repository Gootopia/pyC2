# Collective2 Http
from enum import Enum

import requests


# errors
class Error(Enum):
    ErrNone = 0
    Invalid_URL = -1  # Issue with the C2 URL string.
    Invalid_API_Key = -2  # Issue with the user API key.
    Invalid_System_Id = -3  # Issue with trading system Id


# c2http: Convenience functions for submitting to C2 API
class c2http:
    # used for c2 JSON GET/POST requests
    headers = {'Content-Type': 'application/json'}

    # base URL for submitting all C2 API. All commands append to this string
    apiUrlBase = "https://api.collective2.com/world/apiv3/"

    # developer API key
    apiKey = 'Xo90WkzXt4DtYrhDDRvyMXnaosLUd_yuaT2bZCIJYgmIXwJy0w'

    # C2 Trading System Id
    systemId = 0

    # constructor
    def __init__(self, sysid):
        self.systemId = sysid
        err = self.verifySystem(sysid)

        # Handle any errors
        if err != Error.ErrNone:
            print(str(err))

    # submit POST request to C2 API
    def post(self, function, data):
        return requests.post(self.apiUrlBase + function, headers=self.headers, json=data)

    # Basic header info that must appear in all api packets
    def buildApiPacket(self, id):
        apiPacket = {"systemid": id, "apikey": self.apiKey}
        return apiPacket

    # Method to verify a trading system is valid
    def verifySystem(self, id):
        data = self.buildApiPacket(id)
        c2resp = self.post('getSystemDetails', data).json()

        # If Ok = 0, there was a problem submitting the request
        if c2resp["ok"] == 0:
            return Error.Invalid_URL

        # If the API is ok, we get a "response" JSON field, if not, we get an "error" JSON field
        if "error" in c2resp.keys():
            return Error.Invalid_API_Key

        # System Id must also be correct and accessible from this user
        if c2resp['response']['system_id'] == None:
            return Error.Invalid_System_Id

if __name__ == '__main__':
    print("=== C2 API ===")

    c = c2http(12642394)
    c.verifySystem(126423949)
