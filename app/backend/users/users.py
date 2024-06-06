from app.utils.services.database import Sqlite
from uuid import uuid4
from app.models.users import Client


class Users:
    def __init__(self):
        self.database_handler = Sqlite()

    def __generate_api_key(self):
        return str(uuid4())
    
    def create_client(self, client: Client) -> dict:
        api_key = self.__generate_api_key()
        client = dict(client)
        message, status = self.database_handler.create_client(client['first_name'], client['last_name'], client['email'], api_key)
        if status:
            return {'Status': 'Sucess', 'api_key': api_key}

        return {'Status': 'Fallido', 'Descripcion': message}
