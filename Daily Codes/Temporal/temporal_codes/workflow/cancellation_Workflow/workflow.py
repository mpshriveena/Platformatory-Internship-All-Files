import asyncio
from temporalio import workflow
@workflow.defn
class GreetSomeone():
    @workflow.run
    async def run(self, name:str) -> str:
        try:
            # Simulate some work with periodic cancellation checks
            for i in range(100):
                # Check for cancellation request
                if workflow.is_cancelled():
                    print("Cancellation request received. Stopping workflow.")
                    return  # Gracefully stop the workflow
                
                print(f"{name}! Working... {i+1}/5")
                await asyncio.sleep(1)  # Simulate work with a sleep

            return("Workflow completed successfully.")
        except asyncio.CancelledError:
            # Handle cancellation gracefully if any async operation was canceled
            print("Workflow was cancelled during execution.")
