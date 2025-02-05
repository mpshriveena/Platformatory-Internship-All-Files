from temporalio import activity
@activity.defn
async def greet_in_english(name: str) -> str:
    return f"Hello {name}!"