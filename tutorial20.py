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

## Part 20: Path Operation Configuration

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

class Tags(Enum):
    items = "items"
    users = "users"

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED,
          tags=[Tags.items],
          summary="Create an Item-type item",
          #description="Create an item with all the information: name; description; price; tax; and a set of unique tags"
          response_description="The created item"
          )

async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name":"Foo", "price": 42}]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "murad"}]

@app.get("/elements/", tags=[Tags.items], deprecated =True)
async def read_elements():
    return [{"item_id": "Foo"}]