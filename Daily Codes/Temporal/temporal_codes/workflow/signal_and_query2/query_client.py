import asyncio
from temporalio.client import Client
from workflow import SignalWorkflow

async def query_workflow():
    client = await Client.connect("localhost:7233")  # Adjust for your server
    workflow_id = "products-workflow"
    try:
        queried_result = await client.get_workflow_handle(workflow_id).query(SignalWorkflow.get_product_count)
        print(f"Products left till now is {queried_result}" )
    except Exception as e:
        print(f"Error while canceling workflow: {e}")

asyncio.run(query_workflow())