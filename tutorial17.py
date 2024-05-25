from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta
import uvicorn

from typing import List, Optional, Literal, Union

from starlette.responses import HTMLResponse

app = FastAPI()

## Part 17: Request Files

@app.post("/files/")
async def create_file(files: list[bytes] = File(..., description="A file read as bytes")):
    # if not file:
    #     return {"message": "No file sent"}
    return {"file_sizes": [len(file) for file in files]}

@app.post("/uploadfile/")
async def create_upload_file(files: list[UploadFile] = File(..., description="A file read as UploadFile")):
    # if not file:
    #     return {"message": "No upload file sent"}
    return {"filename": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)