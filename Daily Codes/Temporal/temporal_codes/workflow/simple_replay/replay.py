import asyncio
from temporalio.client import Client, WorkflowHistory
from temporalio.worker import Replayer

async def check_past_histories():
    my_client = await Client.connect("localhost:7233")
    replayer = Replayer(workflows=[greeting-workflow])
    result = await replayer.replay_workflows(
        await my_client.list_workflows("WorkflowType = 'DivideWorkflow'").map_histories(),
    )
    print(f"Replayed Result: {result}")
    return(f"Replayed Result: {result}")

if __name__ == "__main__":
    asyncio.run(check_past_histories())