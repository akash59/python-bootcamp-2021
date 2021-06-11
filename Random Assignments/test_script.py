import os
import requests
import base64

client_id = "IDVsp8LL8gOL6RyujIdCqlxEf7rIUB53"
client_secret = "dlJZYfTfpEWLG9UX+X4gQz+Tq35Wb5Uz"
req = client_id + ":" + client_secret
bString = base64.b64encode(req.encode())
print(bString)


tokenurl = "https://apis-dqa-dcpdare.drtst.org/token"
headers = {
    "Accept": "application/json",
    "Authorization": "Basic " + bString.decode("utf-8"),
}
data = {"grant_type": "client_credentials", "scope": "read"}
response = requests.post(tokenurl, headers=headers, data=data)
respStatus_Code = response.status_code


print(response.text)
print(response.status_code)

if respStatus_Code == 200:
    response_Json = response.json()
    bearer_token = response_Json.get("access_token")
    expires_in = response_Json.get("expires_in")


print(f"Bearer Token value is {bearer_token}")
print(f"Bearer Token expires in {expires_in}")
