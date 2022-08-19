import requests
import streamlit

url = "https://api.web3.storage/upload"

data = {"s":"Avengers Endgame","r":"json","page":"1"}

token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDVFYWQzNjA0Q0I2M0EzMGY5ZEU2MTNDN2VhMDM3M2QyNzFDNjkwMzIiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NjA5MzEwMjk4MDcsIm5hbWUiOiJ0b2tlbiJ9.u1H2NNueEas5Y0QHME2HKl_kuXODtcws93vnkmC8B0k"

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}



response = requests.request("POST", url, auth=token)

print(response.text)
