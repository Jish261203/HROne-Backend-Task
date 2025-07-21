from fastapi import FastAPI
from app.routes import products,orders

app = FastAPI()

@app.get("/")
def root():
    return {"message": "HROne Backend API is running ✅"}

app.include_router(products.router)
app.include_router(orders.router)