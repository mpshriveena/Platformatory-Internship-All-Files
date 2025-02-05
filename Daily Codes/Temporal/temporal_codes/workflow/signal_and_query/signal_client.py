import asyncio
import sys
from temporalio.client import Client
from workflow import ProductsLeft

async def signal_workflow():
    client = await Client.connect("localhost:7233")
    workflow_id = "products-workflow"
    try:
        signalled_result = await client.get_workflow_handle(workflow_id).signal(ProductsLeft.update_products, int(sys.argv[1]))
        print(f"Products updated to {int(sys.argv[1])}" )
    except Exception as e:
        print(f"Error while signalling workflow: {e}")

asyncio.run(signal_workflow())