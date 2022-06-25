from flask_restful import Resource, reqparse
import requests
from models.language import LanguageText


class Language(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = Language.parser.parse_args()
        lang = LanguageText(**data)
        lang.save_to_db()
        return lang.json(), 200
