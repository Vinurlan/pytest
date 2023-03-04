# from quotes import ai_quotes
from flask_restful import Resource, reqparse
import random

ai_quotes = [
    {
        "id": 0,
        "author": "Kevin Kelly",
        "quote": "The business plans of the next 10,000 startups are easy to forecast: "
    },
    {
        "id": 1,
        "author": "Stephen Hawking",
        "quote": "The development of full artificial intelligence could"
    },
    {
        "id": 2,
        "author": "Claude Shannon",
        "quote": "I visualize a time when we will be to robots what "
    },
    {
        "id": 3,
        "author": "Elon Musk",
        "quote": "The pace of progress in artificial intelligence "
    }
]

class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if(quote['id'] == id):
                return quote, 200
        return 'Quote not found',  404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('author')
        parser.add_argument('quote')
        params = parser.parse_args()
        
        for quote in ai_quotes:
            if(id == quote['id']):
                return "Quote with id already exists", 400
        
        quote = {
            'id': int(id),
            'author': params['author'],
            'quote': params['quote']
        }

        ai_quotes.append(quote)
        return quote, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if(id == quote["id"]):
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200
        
        quote = {
            "id": id,
            "author": params["author"],
            "quote": params["quote"]
        }
        
        ai_quotes.append(quote)
        return quote, 201

    def delete(self, id):
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
        return "Quote with id is deleted.", 200