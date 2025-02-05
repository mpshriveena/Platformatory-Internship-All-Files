import json
import asyncio
from temporalio.worker import Replayer
from temporalio.client import WorkflowHistory
from activity_workflow import DivideWorkflow

async def replay_workflow():
    with open("/home/mpshriveena/Desktop/Platformatory/Daily Codes/Temporal/temporal_codes/workflow/replay_workflow_with_error/history.json", "r") as f:
        history_json = json.load(f)
    events = history_json["events"]
    workflow_id = "greeting-workflow"
    history = {
    'events': events
    }
    workflow_history = WorkflowHistory.from_json(workflow_id, history)
    replayer = Replayer(workflows=[DivideWorkflow])
    result = await replayer.replay_workflow(workflow_history)
    #if result.history.events[-1].event_type == "EVENT_TYPE_WORKFLOW_EXECUTION_FAILED":
    #    print("Workflow execution failed")
    failure_message = result.history.events[-1].workflow_execution_failed_event_attributes.failure.message
    failure_cause_message = result.history.events[-1].workflow_execution_failed_event_attributes.failure.cause.message
    failure_type = result.history.events[-1].workflow_execution_failed_event_attributes.failure.cause.application_failure_info.type

    #    print(f"Failure message: {failure_message}")
    #    return
    payload = result.history.events[-1].workflow_execution_completed_event_attributes.result.payloads
    if payload:
        result_data = payload[0].data.decode('utf-8')
        print(f"Replayed Workflow Result: {result_data}")
    else:
        print(f"Replayed Workflow Result: {failure_message}")
        print(f"Type of Failure: {failure_type}")
        print(f"Cause of error: {failure_cause_message}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(replay_workflow())

