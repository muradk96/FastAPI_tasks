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

## Part 22: Dependencies - Intro

async def hello():
    return 'world'

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100, blah: str = Depends(hello)):
    return {"q": q, "skip": skip, "limit": limit, "hello": blah}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons