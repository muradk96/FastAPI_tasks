from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta

from typing import List, Optional, Literal, Union

app = FastAPI()

## Part 16: Form Fields

# class User(BaseModel):
#     username: str
#     password: str

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    print("password", password)
    return {"username": username}

# class User(BaseModel):
#     username: str
#     password: str

@app.post("/login-json/")
async def login_json(username: str = Body(...), password: str = Body(...)):
    print("password", password)
    return {"username": username}