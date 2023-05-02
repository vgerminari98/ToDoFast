import os
import sys
import base64
import config.mongo_connection as con
from pymongo.collection import Collection


class User(Collection):
    def __init__(self, db):
        super().__init__(db,"users")

    @staticmethod
    def encryptb64(password):

        input_bytes = password.encode('utf-8')
        encrypted_bytes = base64.b64encode(input_bytes)
        encrypted_string = encrypted_bytes.decode('utf-8')
        return encrypted_string
    
    @staticmethod
    def generate_user_id():

        # Busca o último ID cadastrado no banco de dados MongoDB
        last_user = con.collection.find_one(sort=[('id', -1)])
        last_id = last_user['_id'] if last_user else 0

        # Incrementa o último ID para gerar o novo ID único
        new_id = last_id + 1
        return new_id

    def create_user(self, name: str, email: str, password: str, is_active=True):
        user = {"name": name,
                "email": email,
                "password": self.encryptb64(password),
                "is_active": is_active,
                "id": self.generate_user_id()}
        
        self.insert_one(user)


#user = User(con.db)
#user.create_user("Fulano", "fulano.detalal@fulas.com", "abelinha123", True, 1)