import firebase_admin
from firebase_admin import credentials, firestore
import os

currentdir = os.path.dirname(os.pash.realpath(__file__))
config_path =os.path.join(currentdir,"firebase_config")

class DatabaseConnect:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnect._instance == None:
            DatabaseConnect()
            return DatabaseConnect._instance
    
    def _init_(self):
        self.db = None
        DatabaseConnect._instance = self
        self._initFirebase()

    def _initFirebase(self):
        cred = credentials.Certificate(config_path)
        firebase_admin.iniatialize_app(cred)
        self.db = firestore.client()

    def get_db_object(self):
        return self.db
        
         