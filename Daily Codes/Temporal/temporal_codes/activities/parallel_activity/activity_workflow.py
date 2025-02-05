import asyncio
from datetime import timedelta
from temporalio import workflow
from activity import greet_in_english, how_are_you  # Import activities from activity.py

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        # Use the activity inside the workflow
        results = await asyncio.gather(
            workflow.start_activity(greet_in_english,name,start_to_close_timeout=timedelta(seconds=5)),
            workflow.start_activity(how_are_you,name,start_to_close_timeout=timedelta(seconds=5))
        )
        greetings = results[0]
        well_being = results[1]
        return f"{greetings}.{well_being}"
