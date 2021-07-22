# Import Packages
from datetime import datetime
import http.client
import mimetypes
import json
import csv

# Timestamp
now = datetime.now()
today = datetime.today()
print("Date Success!")

# Credentials
a = open('./cred.json')
creds = json.load(a)
token = creds['token']
content = creds['type']
url = creds['url']
base = creds['base']
symbol = creds['symbol']
print("Credentials Success!")

# Get Data
conn = http.client.HTTPSConnection(url)
payload = ''
headers = {
    'x-access-token': f'{token}',
    'Content-Type': f'{content}'
}
conn.request("GET", f"/api/{base}/{symbol}", payload, headers)
res = conn.getresponse()
print("GET Success!")

# Status
print(f"API Status: {res.status}")

# Result from JSON
data = json.loads(res.read())
result = data['price']

# Result
print(result)

# Result To CSV
with open("../data/goldprices.csv", "a+", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([now, result])

print("File Success!")