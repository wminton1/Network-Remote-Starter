import requests
#not working, wes
# Your real credentials
FORD_USERNAME = "wminton0001@gmail.com"
FORD_PASSWORD = "@Slattinsen69"
VEHICLE_VIN   = "1FMCU0GN9RUB14440"

CLIENT_ID     = "9fb503e0-715b-47e8-adfd-ad4b7770f73b" 
APP_ID        = "71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592"

print("1. Requesting Token from Ford...")
auth_url = "https://fcis.ice.ibmcloud.com/v1.0/endpoint/default/token"
auth_payload = {
    "client_id": CLIENT_ID, 
    "grant_type": "password",
    "username": FORD_USERNAME, 
    "password": FORD_PASSWORD
}
headers_auth = {
    "User-Agent": "fordpass-na/353 CFNetwork/1121.2.2 Darwin/19.3.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Run the authentication request
auth_response = requests.post(auth_url, data=auth_payload, headers=headers_auth)

if auth_response.status_code == 200:
    access_token = auth_response.json().get("access_token")
    print("Success! Token received.")
    
    print("2. Sending START command to vehicle...")
    start_url = f"https://usapi.cv.ford.com/api/vehicles/{VEHICLE_VIN}/engine/start"
    headers_start = {
        "Content-Type": "application/json",
        "User-Agent": "FordPass/5 CFNetwork/1327.0.4 Darwin/21.2.0",
        "Application-Id": "71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592",
        "auth-token": access_token
    }
    
    start_response = requests.put(start_url, headers=headers_start)
    print(f"Ford Server Response Code: {start_response.status_code}")
else:
    print(f"Failed to authenticate: {auth_response.text}")
