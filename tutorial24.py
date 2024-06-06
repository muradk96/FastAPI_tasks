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


## Part 24: Sub-Dependencies

def query_extractor(q: str | None = None):
    return q

def query_or_body_extractor(q: str = Depends(query_extractor), last_query: str | None = Body(None)):
    if q:
        return q
    return last_query

@app.post("/item")
async def try_query(query_or_body: str = Depends(query_or_body_extractor)):
    return {"q_or_body": query_or_body}