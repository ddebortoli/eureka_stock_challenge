from fastapi import APIRouter, Depends

from app.auth.token import authenticate_user
from app.backend.stock.stock import StockHandler
from app.models.stock import Stock

router = APIRouter()

@router.get("/stock")
def retrieve_stock_detail(current_user: dict = Depends(authenticate_user), stock: Stock = Depends(Stock)):
    stock_handler = StockHandler()
    return stock_handler.get_stock_information(stock)

