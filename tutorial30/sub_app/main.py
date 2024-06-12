from fastapi import Depends, FastAPI

from .dependencies import get_token_header, get_query_token

# todo: import router
# from .routers import users, items
# from .routers.users import router as user_router
# from .routers.items import router as item_router
from .routers import users_router, items_router

app = FastAPI(dependencies=[Depends(get_query_token)])
# app.include_router(users.router)  # users router
# app.include_router(items.router)  # items router
app.include_router(users_router)
app.include_router(items_router)

## Part 30: Bigger Applications - Multiple Files

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

