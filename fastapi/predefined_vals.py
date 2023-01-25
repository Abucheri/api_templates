from fastapi import FastAPI as fp
from enum import Enum as en


# mostly used for path operations that receive a path parameter
# this is when you want for possible valid path parameter values to be predefined
# this will use the predefined Enum class

class ModelName(str, en):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


predef = fp()


@predef.get("/")
async def home():
    return {"welcome": "Predefined Variables"}


@predef.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # You can get the actual value (a str in this case) using model_name.value, or in general, your_enum_member.value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
