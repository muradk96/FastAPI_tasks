import json
from enum import Enum
from typing import Annotated
from uuid import UUID
from datetime import datetime, time, timedelta

from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field, HttpUrl
from pymongo import MongoClient

app = FastAPI()


connection_string = "mongodb+srv://muradDB96:pjPVGLMH2cIcQiuo@atlascluster.qu0yows.mongodb.net/"
client = MongoClient(connection_string)

@app.get("/add_numbers")
async def add_numbers_fct(first_number: float, second_number: float):
    return first_number + second_number

@app.get("/string_value")
async def string_fct(input: str):
    input = list(input)
    reversedString = ""
    for i in range(len(input)-1,-1,-1):
        reversedString = reversedString + input[i]

    return reversedString

class Person(BaseModel):
    name: str
    age: int
    salary: float



@app.post("/payload_body")
async def payload_fct(persons: list[Person]):
    persons_db = client.persons
    persons_collections = persons_db.persons_collections
    print(persons)
    for i in persons:
        persons_collections.insert_one(i.__dict__)
    return persons