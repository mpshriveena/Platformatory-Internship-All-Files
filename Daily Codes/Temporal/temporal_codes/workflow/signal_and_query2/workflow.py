import asyncio
from temporalio import workflow
from typing import List


@workflow.defn
class SignalWorkflow:
    def __init__(self) -> None:
        self._pending_greetings: asyncio.Queue[str] = asyncio.Queue()
        self._exit = False

    @workflow.run
    async def run(self) -> List[str]:
        greetings: List[str] = []
        while True:
            print(f"Greeting: {greetings}")
            await workflow.wait_condition(
                lambda: not self._pending_greetings.empty() or self._exit
            )

            while not self._pending_greetings.empty():
                greetings.append(f"Hello, {self._pending_greetings.get_nowait()}")
                print(f"Greeting: {greetings}")

            if self._exit:
                return greetings

    @workflow.signal
    async def submit_greeting(self, name: str) -> None:
        await self._pending_greetings.put(name)

    @workflow.signal
    def exit(self) -> None:
        self._exit = True


