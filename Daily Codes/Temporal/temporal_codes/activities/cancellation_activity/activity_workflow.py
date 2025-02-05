from datetime import timedelta
from temporalio import workflow
from activity import greet_in_english  # Import activities from activity.py
from temporalio.client import WorkflowFailureError
from temporalio import exceptions

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        try:
        # Use the activity inside the workflow        
            greeting = await workflow.execute_activity(
                greet_in_english,
                name,
                start_to_close_timeout=timedelta(seconds=5),
            )
            return greeting
        except WorkflowFailureError as e:
            # Handle the cancellation of the workflow gracefully
            print(f"Workflow was cancelled: {str(e)}")
            return "Workflow was cancelled."
        except exceptions.CancelledError:
            # Handle cancellation gracefully if any async operation was canceled
            return("Activity was cancelled during execution.")