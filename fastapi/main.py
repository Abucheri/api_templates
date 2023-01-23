from fastapi import FastAPI as fp

# an object/instance for the API, this is the main point of interaction for the APIs
app = fp()


@app.get("/")
async def root():
    return {"message":  "Welcome"}
