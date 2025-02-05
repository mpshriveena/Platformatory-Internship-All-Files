import asyncio
from temporalio import activity
from temporalio import exceptions
@activity.defn
async def greet_in_english(name: str) -> str:
    try:
            # Simulate some work with periodic cancellation checks
                # Check for cancellation request
        if activity.is_cancelled():
            return("Cancellation request received. Stopping activity.")
        await asyncio.sleep(100)
        return("Activity completed successfully.")
    except exceptions.CancelledError:
            # Handle cancellation gracefully if any async operation was canceled
        return("Activity was cancelled during execution.")