import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from activity import greet_in_english
from activity_workflow import GreetingWorkflow
async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(
        client,
        task_queue="greeting-activities",
        workflows=[GreetingWorkflow],
        activities=[greet_in_english],
    )
    await worker.run()
if __name__ == "__main__":
    asyncio.run(main())
