from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta
import uvicorn

from typing import List, Optional, Literal, Union

from starlette.responses import HTMLResponse

app = FastAPI()

## Part 18: Request Forms and Files

@app.post("/files/")
async def create_file(file: bytes = File(...), fileb: UploadFile= File(...), token: str = Form(...), hello: str = Body(...)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
        "hello": hello
    }
