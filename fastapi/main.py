from fastapi import FastAPI as fp
from starlette.responses import JSONResponse

# an object/instance for the API, this is the main point of interaction for the APIs

app = fp()

items = [{"title": "John Wick", "year": 2014}, {"title": "Black Adam", "year": 2022}]


# a decorator to get the root path/url "/" (A "path" is also commonly called an "endpoint" or a "route".)
# tis decoretor tells FastAPI the function that follows is in charge of handling requests that go to the path (/) using the operation (get)
# In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get. It is the "path operation decorator". - from the docs
@app.get("/")
async def root():  # the path operation function which will be called when it receives a request to the IRL (/) with GET operation
    return {
        "message": "Welcome"}  # with this ypo can return a dictionary, list or singular values like strings, int etc...


#  getting all items
@app.get("/items")
def all_items():
    return items


# getting items by id
@app.get("/item/{item_id}")
def individual_item(item_id: int):
    if item_id <= 0:
        return JSONResponse(content={"error": "invalid item id"})
    try:
        item = items[item_id - 1]
    except IndexError:
        return JSONResponse(content = {"error": "item not found..."})
    if item == 0:
        return JSONResponse(content={"error": "item has been deleted"})
    else:
        return JSONResponse(content=item)
