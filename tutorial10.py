from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from enum import Enum

from typing import List, Optional

app = FastAPI()

## Part 10: Declare Request Example Data

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # model_config = {
    #     "json_schema_extra": {
    #         "example":
    #             {
    #             "name": "Foo",
    #             "description": "A very nice Item",
    #             "price": 16.25,
    #             "tax": 1.67
    #         }
    #     }
    # }

@app.put("/items/{item_id")
async def update_item(item_id: int, item: Item = Body(
    ...,
    openapi_examples={
                        "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "description": "test description",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                }
    })):
    results = {"item_id": item_id, "item": item}
    return results
