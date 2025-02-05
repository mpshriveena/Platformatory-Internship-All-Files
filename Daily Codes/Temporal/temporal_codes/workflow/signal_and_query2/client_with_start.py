import asyncio
import sys
from workflow import SignalWorkflow
from temporalio.client import Client
from temporalio.client import WorkflowFailureError

async def main():
    try:
        client = await Client.connect("localhost:7233")
        workflow_handle = await client.start_workflow(
        SignalWorkflow.run,
        id="signal2-workflow",
        task_queue="signal2-tasks",
        start_signal="first_greeting",
        start_signal_args=["User Signal with Start"],
    )
        result = await workflow_handle.result()
        print(f"Workflow finished with result: {result}")
    except WorkflowFailureError as e:
        print(f"Workflow was cancelled or terminated during execution")
    except Exception as e:
        print(f"Error in workflow execution: {str(e)}")
asyncio.run(main())
