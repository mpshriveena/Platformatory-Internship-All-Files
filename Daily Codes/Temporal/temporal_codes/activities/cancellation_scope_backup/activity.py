import re
from temporalio import activity

@activity.defn
async def your_name(name: str,age: int) -> str:
    if is_invalid_name(name):
        raise ValueError(f"Invalid name: {name}")
    upper = name.upper()
    return f"Your name is {upper}!"

@activity.defn
async def your_age(name: str,age: int) -> str:
    if is_invalid_age(age):
        raise ValueError(f"Invalid age: {age}")
    return f"Your age is {age}!"

def is_invalid_name(name: str) -> bool:
    if not re.match("^[A-Za-z]+$", name):
        return True
    return False

def is_invalid_age(age: int) -> bool:
    if(age<=0):
        return True
    return False

