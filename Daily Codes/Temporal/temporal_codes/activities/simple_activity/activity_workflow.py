from datetime import timedelta
from temporalio import workflow
from activity import greet_in_english  # Import activities from activity.py

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        # Use the activity inside the workflow        
        greeting = await workflow.execute_activity(
            greet_in_english,
            name,
            start_to_close_timeout=timedelta(seconds=5),
        )
        return greeting