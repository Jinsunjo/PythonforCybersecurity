import http.client
import json
from urllib import request
from wsgiref.util import request_uri

# The basic api that postman gave me.
conn = http.client.HTTPSConnection("icanhazdadjoke.com")
payload = ''
headers = {}
conn.request("GET", "/search", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))



def getjoke():
    request_uri = "https://icanhazdadjoke.com/search"
    r = request.get(request_uri)
    items = r.json()
    return items

DadJoke = getjoke()

print(getjoke)

print(json.dumps(DadJoke, indent=2))

print("Heres a Joke".format( \
    DadJoke["Joke"])) 