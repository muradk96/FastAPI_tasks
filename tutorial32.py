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

from passlib.context import CryptContext
from jose import jwt, JWTError

# app = FastAPI()

## Part 32: Metadata and Docs URLs

description = """ 
ChimichangAPP API helps you do awesome stuff. 🚀

## Items

You can **read items**

## Users

You will be ablte to:

* **Create users** (_not implemented_).
* ** Read users** (_not implemented_).
"""

tags_metadata= [
    dict(name="users",
         description="Operations with users. The **login** logic is also here."),
    dict(name="items",
         description="Manage items. So _fancy_ they have their own docs.",
         externalDocs=dict(
             description="Items external docs",
             url="http://www.jvp.design"
         ))
]



app = FastAPI(
    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact=dict(name="Deadpoolio the Amazing",
                 url="http://x-force.example.com/contact",
                 email="dp@x-force.example.com"
                 ),
    license_info=dict(
        name="Apache 2.0",
        url="https://www.apache.org/licenses/LICENSE-2.0.html"

    ),
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    docs_url="/hello-world",
    redoc_url=None

)


@app.get("/users", tags=["users"])
async def get_users():
    return [dict(name="Harry"), dict(name="Ron")]

@app.get("/items/", tags=["items"])
async def read_items():
    # return [{"name:": "Katana"}]
    return [dict(name="wand"), dict(name="flying broom")]
