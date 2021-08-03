# Import Packages
from datetime import datetime
import json
import csv
from requests_html import AsyncHTMLSession
import pyppeteer
import asyncio

class Crawler:
    def __init__(self, currency):
        self.currency = currency

    async def crawlerInit(self):

        print(f"Starting File... {self.currency}")

        # Timestamp
        now = datetime.now()
        print("Date success!")

        # Params
        url = f"https://www.gold.org/goldhub/data/gold-prices"
        print("Parameters success!")

        # Crawler
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        session = AsyncHTMLSession()
        browser = await pyppeteer.launch({
            'ignoreHTTPSErrors': True,
            'headless': True,
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False
        })
        session._browser = browser
        r = await session.get(url)
        print("Starting session!")
        script = """
            () => {
                if ( jQuery.isReady ) {
                    $("[data-currency='%s']").click();
                }
            }
        """ % (self.currency)
        await r.html.arender(script=script, wait=4, sleep=4, timeout=20, keep_page=True)
        print("Session started!")

        # Scraper
        print("Grabbing price!")
        xau = r.html.find('.text.value', first=True)
        print(f"{self.currency} {xau.text}")

        r.close()
        await session.close()

        # Result To CSV
        with open("../data/customprices.csv", "a+", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([now, self.currency, xau.text.replace(",","")])

        print("File Success!")

        return {
                'currency': self.currency,
                'price': xau.text.replace(",",""),
            }