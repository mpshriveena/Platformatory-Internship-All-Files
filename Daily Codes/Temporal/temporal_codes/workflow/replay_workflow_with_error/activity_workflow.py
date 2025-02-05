from datetime import timedelta
from temporalio import workflow
from activity import divide  # Import activities from activity.py
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

@workflow.defn
class DivideWorkflow:
    @workflow.run
    async def run(self, a: int, b: int) -> str:
        retry_policy = RetryPolicy(
            maximum_attempts=1
        )     

        answer = await workflow.execute_activity(
            divide,
            args=(a,b),
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy
        )
        return str(answer)

