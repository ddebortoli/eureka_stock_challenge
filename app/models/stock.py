from pydantic import BaseModel
from typing import Optional


class Stock(BaseModel):
    symbol: str
    output_size: str
    mock_data: Optional[str] = ''
