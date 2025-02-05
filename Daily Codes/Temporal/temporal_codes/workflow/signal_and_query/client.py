import asyncio
import sys
from workflow import ProductsLeft
from temporalio.client import Client
from temporalio.client import WorkflowFailureError

async def main():
    try:
        client = await Client.connect("localhost:7233")
        workflow_handle = await client.start_workflow(
        ProductsLeft.run,
        int(sys.argv[1]),
        id="products-workflow",
        task_queue="products-tasks"
    )
        result = await workflow_handle.result()
        print(f"Workflow finished with result: {result}")
    except WorkflowFailureError as e:
        print(f"Workflow was cancelled or terminated during execution")
    except Exception as e:
        print(f"Error in workflow execution: {str(e)}")
asyncio.run(main())
