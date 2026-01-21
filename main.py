from fastapi import FastAPI
from app.routers.orders.order import router as order_router
from app.routers.products.product import router as product_router

import uvicorn

app = FastAPI()
app.include_router(order_router)
app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
