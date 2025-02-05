import logging
from datetime import timedelta
from temporalio import workflow
from activity import greet_in_english

logging.basicConfig(level=logging.DEBUG)

@workflow.defn
class GreetingWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        workflow.logger.info(f"Received input parameter: {name}")
        
        try:
            workflow.logger.debug("Calling greet_in_english activity...")
            greeting = await workflow.execute_activity(
                greet_in_english,
                name,
                start_to_close_timeout=timedelta(seconds=5),
            )
            workflow.logger.info(f"Received greeting: {greeting}")
            return greeting
        except Exception as e:
            workflow.logger.error(f"An error occurred: {str(e)}")
            raise



