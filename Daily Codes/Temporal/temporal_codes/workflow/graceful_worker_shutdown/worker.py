import asyncio
import signal
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import GreetSomeone

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(client, task_queue="greeting-tasks", workflows=[GreetSomeone])
    shutdown_event = asyncio.Event()
    def signal_handler():
        print("Received Ctrl+C, initiating graceful shutdown...")
        shutdown_event.set()
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, signal_handler)
    worker_task = asyncio.create_task(worker.run())
    try:
        await shutdown_event.wait()
    finally:
        print("Shutting down worker...")
        await worker.shutdown()
        print("Worker shutdown complete")

if __name__ == "__main__":
    asyncio.run(main())