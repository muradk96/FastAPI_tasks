from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile, HTTPException, Request
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta
import uvicorn

from typing import List, Optional, Literal, Union

from starlette.responses import HTMLResponse
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler

app = FastAPI()


## Part 21: JSON Compatible Encoder and Body Updates

#fake_db = {}

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []
    # title: str
    # timestamp: datetime

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "bass": {"name": "Bass", "description": None, "price": 50.2, "tax": 10.5, "tags":[]}
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items.get(item_id)

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatible_item_data
#     print(fake_db)
#     return "Success"

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app.patch("/items/{item_id}", response_model=Item)
def patch_item(item_id: str, item: Item):
    stored_item_data = items.get(item_id)
    if stored_item_data is not None:
        stored_item_model = Item(**stored_item_data)
    else:
        stored_item_model = Item()
    update_data = item.dict(exclude_unset=True)
    # print("update_data", update_data)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    print(items[item_id])
    return updated_item
