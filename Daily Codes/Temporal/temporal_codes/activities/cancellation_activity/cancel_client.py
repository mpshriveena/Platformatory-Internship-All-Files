import asyncio
from temporalio.client import Client

async def cancel_workflow():
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")  # Adjust for your server

    # Workflow ID of the running workflow to cancel
    workflow_id = "greeting-workflow"

    try:
        # Get the workflow handle using the workflow ID

        # Cancel the workflow execution
        await client.get_workflow_handle(workflow_id).cancel()

        print(f"Cancellation request has been sent to Workflow {workflow_id}")

    except Exception as e:
        print(f"Error while canceling workflow: {e}")

# Run the cancel function
asyncio.run(cancel_workflow())