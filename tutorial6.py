from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from enum import Enum

from typing import List, Optional

app = FastAPI()

## Part 6: Path Parameters and Numeric Validation

@app.get("/items_validation/{item_id}")
async def read_items_validation(*, item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100), q:str = "hello",
                                size: float = Query(..., gt=0, lt=7.75)


                                ):
    results = {"item_id": item_id, "size": size}
    if q:
        results.update({"q": q})
    return results