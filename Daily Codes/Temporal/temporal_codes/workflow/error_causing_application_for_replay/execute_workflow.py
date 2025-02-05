import asyncio
import sys
from temporalio.client import Client
from activity_workflow import DivideWorkflow  # Import your workflow
async def main():
    client = await Client.connect("localhost:7233")
    # Start the workflow
    handle = await client.start_workflow(
        DivideWorkflow.run,  # Workflow function
        args=(int(sys.argv[1]), int(sys.argv[2])),
        id="greeting-workflow",  # Workflow ID
        task_queue="greeting-activities"  # Task queue
    )   
    print(f"Started workflow. Workflow ID: {handle.id}, RunID: {handle.result_run_id}")
    # Wait for the result of the workflow
    result = await handle.result()
    print(f"Result: {result}")
if __name__ == "__main__":
    asyncio.run(main())
    

