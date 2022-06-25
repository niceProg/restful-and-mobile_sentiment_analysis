from common.db import db
import requests


class LanguageText(db.Model):
    __tablename__ = 'LanguageText'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, text):
        self.text = text

    def json(self):
        params = {'access_key': '12525a4a8f71d1952ad454c2df7061cb', "query": self.text}
        languages = requests.get('http://apilayer.net/api/detect', params=params).json()

        if languages['success']:
            return languages
        else:
            return {"message": "Can't detect"}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



