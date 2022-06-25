from flask import Flask
from flask_restful import Api

from resources.language import Language
from resources.sentiment import SentimentAnalysis
from common.db import db

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'VqLf794gDvyT9FxwZWJzpTnGZXtOGrTeWeR1HX0dz338NmivPU'
api = Api(app)

api.add_resource(SentimentAnalysis, '/sentiment')
api.add_resource(Language, '/language')

if __name__ == '__main__':
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
