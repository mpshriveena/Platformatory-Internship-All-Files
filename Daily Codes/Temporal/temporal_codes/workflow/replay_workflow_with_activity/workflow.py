from temporalio import workflow
@workflow.defn
class GreetingWorkflow():
    @workflow.run
    async def run(self, name:str) -> str:
        return f"Hello {name}!"
