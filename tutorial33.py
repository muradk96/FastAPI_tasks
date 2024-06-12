from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile, HTTPException, Request, Depends, BackgroundTasks
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta
import time
import uvicorn

from typing import List, Optional, Literal, Union

from starlette.responses import HTMLResponse
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from passlib.context import CryptContext
from jose import jwt, JWTError

app = FastAPI()


## Part 33: Static Files, Testing, and Debugging

# app.mount("/static", StaticFiles(directory="static"), name="static")

fake_secret_token = "coneofsilence"
fake_db = dict(
    foo=dict(
        id="foo", title="Foo", description="There goes my hero",
    ),
    bar=dict(
        id="bar", title="Bar", description="The bartenders"
    )
)


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item