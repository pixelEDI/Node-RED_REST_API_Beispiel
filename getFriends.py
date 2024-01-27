import requests

url="https://nodered.ipv64.net/myfriends?token=mysecret&id=3"

response = requests.get(url)

if(response.status_code)== 200:
    print(response.text)
else:
    print("Error -> Keine Daten")