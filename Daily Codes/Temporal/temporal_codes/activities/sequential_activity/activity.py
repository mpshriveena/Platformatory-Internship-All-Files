from temporalio import activity

@activity.defn
async def upper_case(name: str) -> str:
    upper = name.upper()
    return f"{upper}!"

@activity.defn
async def greet_in_english(name: str) -> str:
    return f"Hello {name}!"