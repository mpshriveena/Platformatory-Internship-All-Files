import asyncio
import sys
from temporalio.client import Client
from temporalio.client import WorkflowFailureError
from temporalio.exceptions import ActivityError
from activity_workflow import GreetingWorkflow  # Import your workflow
async def main():
    try:
        client = await Client.connect("localhost:7233")
    # Start the workflow
        handle = await client.start_workflow(
            GreetingWorkflow.run,
            args=(sys.argv[1], int(sys.argv[2])),
            id="greeting-workflow",
            task_queue="greeting-activities",
        )
        print(f"Started workflow. Workflow ID: {handle.id}, RunID: {handle.result_run_id}")
    # Wait for the result of the workflow
        result = await handle.result()
        print(f"Result: {result}")
    except WorkflowFailureError as e:
        # Workflow cancellation can trigger a WorkflowFailureError
        print(f"Workflow was cancelled or terminated during execution")
    except ActivityError as e:
        # Handle any other client-side exceptions
        print(f"Error in workflow execution: {str(e)}")
if __name__ == "__main__":
    asyncio.run(main())

