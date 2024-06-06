from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile, HTTPException, Request, Depends
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

## Part 23: Classes as Dependencies

# class Cat:
#     def __init__(self, name: str):
#         self.name = name
#
# fluffy = Cat("Mr Fluffy")

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Bass"}]

class CommonQueryParams:
    def __init__(self, item_id: int, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
        # self.item_id = item_id

@app.get("/items/{item_id}")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    #print(commons.item_id)
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
