import re
from temporalio import activity

@activity.defn
async def your_name(name: str) -> str:
    if is_invalid_name(name):
        raise ValueError(f"Invalid name: {name}")
    upper = name.upper()
    return f"Your name is {upper}!"

def is_invalid_name(name: str) -> bool:
    if not re.match("^[A-Za-z]+$", name):
        return True
    return False


