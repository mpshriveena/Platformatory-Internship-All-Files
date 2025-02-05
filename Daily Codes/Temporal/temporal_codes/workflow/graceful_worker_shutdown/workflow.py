from temporalio import workflow
@workflow.defn
class GreetSomeone():
    @workflow.run
    async def run(self, name:str) -> str:
        print(f"Received input name :{name}")
        return f"Hello {name}!"
