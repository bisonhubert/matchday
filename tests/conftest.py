import pytest

from matchday import dataclasses


class Matchday1:
    MATCH_RECORD_1 = "San Jose Earthquakes 3, Santa Cruz Slugs 3\n"
    MATCH_RECORD_2 = "Capitola Seahorses 1, Aptos FC 0"
    MATCH_RECORD_3 = "Felton Lumberjacks 2, Monterey United 0"


class Matchday2:
    MATCH_RECORD_1 = "Felton Lumberjacks 1, Aptos FC 2\n"
    MATCH_RECORD_2 = "Santa Cruz Slugs 0, Capitola Seahorses 0"
    MATCH_RECORD_3 = "Monterey United 4, San Jose Earthquakes 2"


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
def match_records_1():
    return [
        Matchday1.MATCH_RECORD_1,
        Matchday1.MATCH_RECORD_2,
        Matchday1.MATCH_RECORD_3,
    ]


@pytest.fixture
def match_records_2():
    return [
        Matchday2.MATCH_RECORD_1,
        Matchday2.MATCH_RECORD_2,
        Matchday2.MATCH_RECORD_3,
    ]


@pytest.fixture
def multiple_matchday_records():
    return [
        Matchday1.MATCH_RECORD_1,
        Matchday1.MATCH_RECORD_2,
        Matchday1.MATCH_RECORD_3,
        Matchday2.MATCH_RECORD_1,
        Matchday2.MATCH_RECORD_2,
        Matchday2.MATCH_RECORD_3,
    ]


@pytest.fixture
def match_record_1():
    return Matchday1.MATCH_RECORD_1


@pytest.fixture
def match_record_2():
    return Matchday1.MATCH_RECORD_2


@pytest.fixture
def match_record_3():
    return Matchday1.MATCH_RECORD_3


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
