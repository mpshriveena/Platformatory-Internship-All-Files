from datetime import timedelta
from temporalio import workflow
from temporalio.exceptions import ActivityError, CancelledError
from temporalio.common import RetryPolicy
from activity import your_name  # Import activities from activity.py

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        # Use the activity inside the workflow
        retry_policy = RetryPolicy(
            maximum_attempts=1
        )  
        try:
            activity1_handle = await workflow.execute_activity(
            your_name,
            name,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy = retry_policy
            )
            return_name = activity1_handle
        except ActivityError as e:
            return_name="Invalid name"
            return f"{return_name}"
        return f"{return_name}"
    
    