from flask import Flask
from flask_restful import Api
from classes.Quote import Quote

app = Flask(__name__)
api = Api(app)

app.config['ENV'] = 'prodaction'
app.config['APP'] = 'prodaction'

api.add_resource(Quote, '/ai-quotes', '/ai-quotes/', '/ai-quotes/<int:id>')
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5000')