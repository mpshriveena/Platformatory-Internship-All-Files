import json
import asyncio
from temporalio.worker import Replayer
from temporalio.client import WorkflowHistory
from workflow import GreetSomeone

async def replay_workflow():
    with open("/home/mpshriveena/Desktop/Platformatory/Daily Codes/Temporal/temporal_codes/workflow/replay_workflow/history.json", "r") as f:
        history_json = json.load(f)
    events = history_json["events"]
    workflow_id = "greeting-workflow"
    history = {
    'events': events
    }
    workflow_history = WorkflowHistory.from_json(workflow_id, history)
    replayer = Replayer(workflows=[GreetSomeone])
    result = await replayer.replay_workflow(workflow_history)
    payload = result.history.events[-1].workflow_execution_completed_event_attributes.result.payloads
    result_data = payload[0].data.decode('utf-8')

    print(f"Replayed Workflow Result: {result_data}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(replay_workflow())

