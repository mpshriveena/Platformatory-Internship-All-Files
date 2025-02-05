import asyncio
import sys
from temporalio.client import Client
from workflow import SignalWorkflow

async def signal_workflow():
    client = await Client.connect("localhost:7233")
    workflow_id = "signal2-workflow"
    try:
        signalled_result = await client.get_workflow_handle(workflow_id).signal(SignalWorkflow.exit)
        print(f"Exited" )
    except Exception as e:
        print(f"Error while signalling workflow: {e}")

asyncio.run(signal_workflow())