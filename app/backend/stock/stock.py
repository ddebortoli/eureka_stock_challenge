from app.models.stock import Stock
from app.utils.services.alphavantage import AlphaVantage
from app.utils.decrypt import decrypt_file, load_key
from json import loads
from logging import info


class StockHandler:
    def __init__(self):
        alpha_variables = decrypt_file('variables.enc', load_key())
        alpha_variables = loads(alpha_variables)
        self.alpha_handler = AlphaVantage(alpha_variables)

    def get_stock_information(self, stock: Stock) -> dict:
        stock = dict(stock)
        stock_information = {}
        if stock.get('mock_data'):
            info('Using MOCK retrieve stock information')
            with open('app/mock/stock_data.json', 'r') as file:
                stock_information = loads(file.read())
        else:
            stock_information = self.alpha_handler.retrieve_stock_information(stock['symbol'], stock['output_size'])

        return stock_information
