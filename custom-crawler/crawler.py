# Import Packages
from datetime import datetime
import json
import csv
from requests_html import HTMLSession

# Timestamp
now = datetime.now()
print("Date success!")

# Params
currency = input("Select a currency (USD, EUR, GBP etc.): ").upper()
url = f"https://www.gold.org/goldhub/data/gold-prices"
print("Parameters success!")

# Crawler
session = HTMLSession()
r = session.get(url)
print("Starting session!")
script = """
    () => {
        $(document).ready(function() {
            $("[data-currency='%s']").click();
        })
    }
""" % (currency)
r.html.render(script=script, wait=2, sleep=4, timeout=20)
print("Session started!")

# Scraper
print("Grabbing price!")
xau = r.html.find('.text.value', first=True)
print(f"{currency} {xau.text}")

r.close()
session.close()

# Result To CSV
with open("../data/customprices.csv", "a+", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow([now, currency, xau.text.replace(",","")])

print("File Success!")