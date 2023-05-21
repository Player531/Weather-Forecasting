import requests
import json

api_key = "API KEY" #Enter Your IP Base api key
ip_address = "IP Address" #Enter Your IP address

api_endpoint = "https://api.ipbase.com/v2/info"
query_params = {"apikey": api_key}

if ip_address:
    query_params["ip"] = ip_address

response = requests.get(api_endpoint, params=query_params)
if response.status_code == 200:
    data = response.json()
    try:
        city_name = data['data']['location']['city']['name']
        print("City:",city_name)
    except KeyError as e:
        print(f"ERROR: {e}")
    # print(json.dumps(data, indent=2))
else:
    print(f"ERROR: {requests.status_code} - {response.text}")

Status_Endpoint = "https://api.ipbase.com/v2/status" #This will tell you how many API calls you have remaining
response = requests.get(Status_Endpoint, params=query_params)
result = response.json()
total = result["quotas"]["month"]["total"]
used = result["quotas"]["month"]["used"]
remaining = result["quotas"]["month"]["remaining"]

print(f"Total Requests: {total}")
print(f"Used Requests: {used}")
print(f"Remaining Requests: {remaining}\n")
