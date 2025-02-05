import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from activity import divide
from activity_workflow import DivideWorkflow
async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(
        client,
        task_queue="greeting-activities",
        workflows=[DivideWorkflow],
        activities=[divide],
    )
    await worker.run()
if __name__ == "__main__":
    asyncio.run(main())
