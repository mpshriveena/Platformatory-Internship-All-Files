from temporalio import activity

@activity.defn
async def greet_in_english(name: str) -> str:
    return f"Hello {name}!"

@activity.defn
async def how_are_you(name: str) -> str:
    return f"How are you, {name}?"