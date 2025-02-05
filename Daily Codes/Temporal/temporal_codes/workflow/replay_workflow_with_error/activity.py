from temporalio import activity

@activity.defn
async def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b