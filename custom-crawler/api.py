from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from crawler import Crawler
import asyncio

# Start Flask API
app = Flask(__name__)
api = Api(app)

# Create endpoints
class Prices(Resource):
    def get(self):
        # Parser
        parser = reqparse.RequestParser()
        parser.add_argument('currency', required=True)
        args = parser.parse_args()

        currency = {'currency': args['currency']}
        print(currency)

        # Import Data
        data = pd.DataFrame(pd.read_csv('../data/customprices.csv', index_col=False, sep=','))
        # Get data for currency
        data = data.loc[data['currency'] == str(currency['currency'])]
        data = data.loc[data['date'] == data['date'].iloc[-1]]
        # Output data
        data = data.to_dict(orient='records')
        return {'data': data}, 200

    def post(self):
        # Parser
        parser = reqparse.RequestParser()
        parser.add_argument('currency', required=True)
        args = parser.parse_args()

        data = {'currency': args['currency']}
        print(data)

        # Crawler
        loop = asyncio.new_event_loop()
        print("Running...")
        crawler = Crawler(str(data['currency']))
        task = loop.create_task(crawler.crawlerInit())
        loop.run_until_complete(task)
        print("Finished!")

        return task.result(), 200

api.add_resource(Prices, '/prices')

if __name__ == '__main__':
    app.run()