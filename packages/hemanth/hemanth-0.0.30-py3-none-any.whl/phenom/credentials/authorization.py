from phenom.credentials.get_token import tokengeneration
from phenom.credentials.methods import Methods
class Authorization(object):
    def __init__(self, url, clientid, clientsecret):
        self.token = tokengeneration(url, clientid, clientsecret)
        self.resume = Methods(self.token)
        self.prediction = Methods(self.token)
