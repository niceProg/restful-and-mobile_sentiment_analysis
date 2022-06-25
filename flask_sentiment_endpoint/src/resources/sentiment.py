from flask_restful import Resource, reqparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalysis(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = SentimentAnalysis.parser.parse_args()
        text = data['text']
        print(text)
        sid = SentimentIntensityAnalyzer()
        sentiment = sid.polarity_scores(text)

        return sentiment, 200
