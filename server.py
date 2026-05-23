import requests

url = "https://google.com"  

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Server is Running")
    else:
        print("Server is Not Running")

except:
    print("Server is Not Reachable")