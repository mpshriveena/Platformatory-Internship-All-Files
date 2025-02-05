from datetime import timedelta
from temporalio import workflow
from temporalio.exceptions import ActivityError, CancelledError
from temporalio.common import RetryPolicy
from activity import your_name,your_age  # Import activities from activity.py
from temporalio.client import WorkflowFailureError

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str, age: int) -> str:
        # Use the activity inside the workflow
        retry_policy = RetryPolicy(
            maximum_attempts=1
        ) 
        try:
            activity1_handle = workflow.start_activity(
            your_name,
            args=(name,age),
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy = retry_policy
            )
            return_name = await activity1_handle
        except ActivityError as e:
            print(f"Activity1 failed: {e}")
            return_name="Invalid name"
            activity1_handle.cancel()
            print(f"Cancelled Activity 1")
        try:
            activity2_handle = workflow.start_activity(
            your_age,
            args=(name,age),
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy = retry_policy
            )
            return_age = await activity2_handle
        except ActivityError as e:
            print(f"Activity2 failed: {e}")
            return_age="Invalid age"
            activity2_handle.cancel()
            print(f"Cancelled Activity 2")

        return f"{return_name}.{return_age}"
    
    