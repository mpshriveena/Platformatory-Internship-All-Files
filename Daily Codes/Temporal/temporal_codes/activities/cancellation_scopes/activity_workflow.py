import re
from datetime import timedelta
from temporalio import workflow
from temporalio.exceptions import ActivityError, CancelledError
from temporalio.client import WorkflowFailureError
from temporalio.common import RetryPolicy
from activity import your_name,your_age  # Import activities from activity.py


@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str, age: int) -> str:
        # Use the activity inside the workflow
        try:
            activity1_handle = workflow.start_activity(
            your_name,
            args=(name,age),
            start_to_close_timeout=timedelta(seconds=5),
            )
            if not re.match("^[A-Za-z]+$", name):
                print(f"There is a special character in your name. It is invalid.")
                activity1_handle.cancel()
                print(f"So the activity 1 is cancelled")
                
            return_name = await activity1_handle
            print(f"return_name:{return_name}")
        except WorkflowFailureError as e:
            print(f"Activity1 failed: {e}")
            return_name="Invalid name"
            activity1_handle.cancel()
            print(f"Cancelled Activity 1")
        try:
            activity2_handle = workflow.start_activity(
            your_age,
            args=(name,age),
            start_to_close_timeout=timedelta(seconds=5),
            )
            if(age<=0):
                print(f"The age is less than or equal to 0. It is invalid")
                activity2_handle.cancel()
                print(f"So the activity 2 is cancelled")
                
            return_age = await activity2_handle
            print(f"return_age:{return_age}")
        except WorkflowFailureError as e:
            print(f"Activity2 failed: {e}")
            return_age="Invalid age"
            activity2_handle.cancel()
            print(f"Cancelled Activity 2")

        return f"{return_name}.{return_age}"
    
    