from fastapi import FastAPI
from items import router as items_router
from users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)

# router
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # /items/123?q=John Q부분은 뒤에 붙는 쿼리
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}





if __name__ == "__main__":
    # ASGI 서버
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")


