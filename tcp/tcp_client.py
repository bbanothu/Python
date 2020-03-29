# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://127.0.0.1:5000/sendMessage"


while 1:
    MESSAGE = str(raw_input("Enter your first message : "))
    PARAMS = {'message':MESSAGE} 
    r = requests.get(url = URL, params = PARAMS) 
    print r.text
    if MESSAGE == "Quit":
        break
print "Session has ended"