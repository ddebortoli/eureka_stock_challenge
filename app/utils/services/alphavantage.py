from requests import request
from typing import Dict
from logging import info, error


class AlphaVantage:
    def __init__(self, company_variables: dict):
        self.company_variables = company_variables

    def retrieve_stock_information(self, symbol: str, output_size: str = 'compact', interval: str = '5min') -> Dict:
        """retrieve stock information from alphavantage endpoint.

        Args:
            symbol (str): company's symbol
            output_size (str, optional): outputsize. Defaults to 'compact'.
            interval (str, optional): time interval. Defaults to '5min'.

        Returns:
            Dict: Full data information about the stock.
        """
        stock_data = {}
        info('About to execute GET stock information')
        url = self.company_variables['base_url']
        params = {
            'symbol': symbol,
            'output_size': output_size,
            'function': 'TIME_SERIES_INTRADAY',
            'interval': interval,
            'apikey': self.company_variables['api_key']
        }
        response = request("GET", url, headers={}, params=params)
        status_code = response.status_code
        info(f'GET Stock information status code: {status_code}')
        if status_code == 200:
            stock_data = response.json()
        else:
            error(f'GET Stock error: {response.content}')

        return stock_data
