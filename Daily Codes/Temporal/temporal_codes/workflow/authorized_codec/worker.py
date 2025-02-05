import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import GreetSomeone
from codec import EncryptionCodec
import temporalio
import dataclasses
async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=dataclasses.replace(
                temporalio.converter.default(), payload_codec=EncryptionCodec()
        ),
)
    worker = Worker(client, task_queue="greeting-tasks", workflows=[GreetSomeone])
    await worker.run()
if __name__ == "__main__":
    asyncio.run(main())
