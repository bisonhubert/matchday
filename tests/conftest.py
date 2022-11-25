import pytest

from matchday import dataclasses

MATCH_RECORD_1 = "San Jose Earthquakes 3, Santa Cruz Slugs 3\n"
MATCH_RECORD_2 = "Capitola Seahorses 1, Aptos FC 0"
MATCH_RECORD_3 = "Felton Lumberjacks 0, Monterey United 2"

INVALID_MATCH_RECORD_1 = ""
INVALID_MATCH_RECORD_2 = "0"
INVALID_MATCH_RECORD_3 = "Felton"
INVALID_MATCH_RECORD_4 = "Felton Lumberjacks"
INVALID_MATCH_RECORD_5 = "Felton Lumberjacks, Aptos FC 0"
INVALID_MATCH_RECORD_6 = "Aptos FC 0, "
INVALID_MATCH_RECORD_7 = "Aptos FC 0, 0"
INVALID_MATCH_RECORD_8 = "Aptos FC 0, Felton"
INVALID_MATCH_RECORD_9 = "Aptos FC 0, 0 Felton"
INVALID_MATCH_RECORD_10 = "Felton Lumberjacks 0,Monterey United 2"


@pytest.fixture
def match_record_1():
    return MATCH_RECORD_1


@pytest.fixture
def match_record_2():
    return "Capitola Seahorses 1, Aptos FC 0"


@pytest.fixture
def match_record_3():
    return "Felton Lumberjacks 0, Monterey United 2"


@pytest.fixture
def invalid_match_records():
    return [
        INVALID_MATCH_RECORD_1,
        INVALID_MATCH_RECORD_2,
        INVALID_MATCH_RECORD_3,
        INVALID_MATCH_RECORD_4,
        INVALID_MATCH_RECORD_5,
        INVALID_MATCH_RECORD_6,
        INVALID_MATCH_RECORD_7,
        INVALID_MATCH_RECORD_8,
        INVALID_MATCH_RECORD_9,
        INVALID_MATCH_RECORD_10,
    ]


@pytest.fixture
def soccer_match():
    return dataclasses.SoccerMatch(
        original_record="San Jose Earthquakes 3, Santa Cruz Slugs 3\n"
    )
