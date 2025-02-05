import asyncio
import sys
from temporalio.client import Client
from activity_workflow import GreetingWorkflow  # Import your workflow
async def main():
    client = await Client.connect("localhost:7233")
    # Start the workflow
    handle = await client.start_workflow(
        GreetingWorkflow.run,
        sys.argv[1],
        id="greeting-workflow",
        task_queue="greeting-activities",
    )    
    print(f"Started workflow. Workflow ID: {handle.id}, RunID: {handle.result_run_id}")
    # Wait for the result of the workflow
    result = await handle.result()
    print(f"Result: {result}")
if __name__ == "__main__":
    asyncio.run(main())
