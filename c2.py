# Collective2 Functions
import requests


# sysid = 126423949

class c2:
    apikey = ''

    # Constructor
    def __init__(self, apikey="Xo90WkzXt4DtYrhDDRvyMXnaosLUd_yuaT2bZCIJYgmIXwJy0w"):
        self.apikey = apikey
        print("Collective2key is:" + self.apikey)

    # r = requests.post("https://api.collective2.com/world/apiv3/submitSignal", headers=headers, json=data)
    # print(r.json())
