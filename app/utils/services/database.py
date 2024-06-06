import sqlite3
from typing import Tuple
from logging import info, error


class Sqlite:
    def __init__(self):
        self.conn = sqlite3.connect('stock-market-service.db')

    def get_access_by_client_api_key(self, api_key: str) -> dict:
        """Obtains data if api_key is associated to a client.

        Args:
            api_key (str): apikey generated in create_client

        Returns:
            dict: True if sucess, empty if fail.
        """
        result_dict = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT True from clients WHERE api_key = ?', (api_key,))

            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            
            for row in rows:
                for i, column_name in enumerate(column_names):
                    result_dict[column_name] = row[i]
        except Exception as e:
            message = f'Error while executing get_access_by_client_api_key: {e}' 
            error(message)
        finally:
            self.conn.close()

        if not result_dict:
            error('No data was found for current apikey')

        return result_dict

    def get_user_data(self, token: str) -> dict:
        """Get data from users (upper credentials) if token is valid.

        Args:
            token (str): jwt token uplodead to the table.

        Returns:
            dict: True if sucess. Empty if failure.
        """
        result_dict = {}
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT True from users WHERE token = ?', (token,))

            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            for row in rows:
                for i, column_name in enumerate(column_names):
                    result_dict[column_name] = row[i]
        except Exception as e:
            message = f'Error while executing get_user_data: {e}' 
            error(message)
        finally:
            self.conn.close()

        if not result_dict:
            error('No data was found for current token')

        return result_dict
    
    def create_client(self, first_name: str, last_name: str, email: str, api_key: str) -> Tuple[str, bool]:
        """Get data from users (upper credentials) if token is valid.

        Args:
            first_name (str): user first name.
            last_name (str): user last name.
            email (str): user email (unique)
            api_key (str): api key to upload

        Returns:
            Tuple[str, bool]: Message if failure, True if sucess
        """
        info(f'Generating new user with mail {email}')
        cursor = self.conn.cursor()
        try:
            query = """INSERT INTO clients (first_name, last_name, email, api_key)
            VALUES(?,?,?,?)"""
            cursor.execute(query,(first_name, last_name, email, api_key))
            self.conn.commit()
        except Exception as e:
            message = f'Error while executing create_client: {e}' 
            error(message)
            return message, False
        else:
            info('User generated sucessfully.')
        finally:
            self.conn.close()
        
        
        return 'Creacion exitosa', True
