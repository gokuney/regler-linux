from .config import config
from firebase_admin import db
import firebase_admin, os


class Firebase:
    def __init__(self):
        print("inited Firebase")
        self.cred_obj = firebase_admin.credentials.Certificate(os.path.abspath(os.path.dirname(__file__))+'/firebase.json')
        self.default_app = firebase_admin.initialize_app(self.cred_obj, {
	        'databaseURL': config["DATABASE_URL"]
	        })

    def instance(self):
        return firebase_admin.db
