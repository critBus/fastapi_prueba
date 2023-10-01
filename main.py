from fastapi import FastAPI, HTTPException
from typing import Union,Dict,List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
from typing import List, Dict

def process_orders(orders: List[Dict[str, any]], criterion: str) -> float:
    filtered_orders = []
    for order in orders:
        if criterion == "completed" and order["status"] == "completed":
            filtered_orders.append(order)
        elif criterion == "pending" and order["status"] == "pending":
            filtered_orders.append(order)
        elif criterion == "canceled" and order["status"] == "canceled":
            filtered_orders.append(order)
        elif criterion == "all":
            filtered_orders.append(order)
    total_revenue = 0.0
    for order in filtered_orders:
        total_revenue += order["quantity"] * order["price"]
    return total_revenue
class Orden(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

class Pedido(BaseModel):
    orders: List[Orden]
    criterion: str

@app.post("/solution")
async def solution(pedido:Pedido):
    for orden in pedido.orders:
        if orden.price<0:
            raise HTTPException(status_code=400,
                                detail="Invalid price. Expected price>0")
        if orden.quantity<0:
            raise HTTPException(status_code=400,
                                detail="Invalid quantity. Expected quantity>0")
    orders = [order.model_dump() for order in pedido.orders]
    criterion = pedido.criterion
    if criterion not in ["completed", "pending", "canceled", "all"]:
        raise HTTPException(status_code=400,
                            detail="Invalid criterion. Expected 'completed', 'pending', 'canceled' or 'all'.")
    return process_orders(orders=orders,criterion=criterion)

