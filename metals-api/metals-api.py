# Import Packages
from datetime import datetime
import requests
import json
import csv

# Timestamp
now = datetime.now()
print("Date Success!")

# Credentials
a = open('./cred.json')
creds = json.load(a)
url = creds['url']
token = creds['token']
content = creds['type']
base = creds['base']
symbolsList = creds['symbols']
symbols = ','.join(symbolsList)
print("Credentials Success!")

# Get Data
r = requests.get(f"{url}?access_key={token}&base={base}&symbols={symbols}")

# Status
print(f"API Status: {r.status_code}")

# Result from JSON
data = json.loads(r.text)
result = round(data['rates']['USD'],2)

# Result
print(result)

# Result To CSV
with open("../data/goldprices.csv", "a+", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([now, result])

print("File Success!")