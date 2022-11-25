import pytest

from matchday import dataclasses


@pytest.fixture
def soccer_match():
    return dataclasses.SoccerMatch(
        original_record="San Jose Earthquakes 3, Santa Cruz Slugs 3\n"
    )
