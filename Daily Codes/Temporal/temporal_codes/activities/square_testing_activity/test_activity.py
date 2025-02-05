import pytest
from temporalio.testing import ActivityEnvironment
from activity import SquareActivities

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input, output",
    [(5, 25), (-5, 25), (2, 4), (-3, 9), (-4, 16)],
)
async def test_square(input, output):
    activity_environment = ActivityEnvironment()
    activities = SquareActivities()
    assert output == await activity_environment.run(activities.square, input)
    print(f"Output: {output}")
