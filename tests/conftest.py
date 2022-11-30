import pytest

from matchday import dataclasses


class Matchday1:
    MATCH_RECORD_1 = "San Jose Earthquakes 3, Santa Cruz Slugs 3"
    MATCH_RECORD_2 = "Capitola Seahorses 1, Aptos FC 0"
    MATCH_RECORD_3 = "Felton Lumberjacks 2, Monterey United 0"


class Matchday2:
    MATCH_RECORD_1 = "Felton Lumberjacks 1, Aptos FC 2"
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


def format_match_record(match_record):
    return f"{match_record}\n"


@pytest.fixture
def match_records_1():
    return [
        format_match_record(Matchday1.MATCH_RECORD_1),
        format_match_record(Matchday1.MATCH_RECORD_2),
        Matchday1.MATCH_RECORD_3,
    ]


@pytest.fixture
def match_records_2():
    return [
        format_match_record(Matchday2.MATCH_RECORD_1),
        format_match_record(Matchday2.MATCH_RECORD_2),
        Matchday2.MATCH_RECORD_3,
    ]


@pytest.fixture
def multiple_matchday_records():
    return [
        format_match_record(Matchday1.MATCH_RECORD_1),
        format_match_record(Matchday1.MATCH_RECORD_2),
        format_match_record(Matchday1.MATCH_RECORD_3),
        format_match_record(Matchday2.MATCH_RECORD_1),
        format_match_record(Matchday2.MATCH_RECORD_2),
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
        format_match_record(INVALID_MATCH_RECORD_1),
        format_match_record(INVALID_MATCH_RECORD_2),
        format_match_record(INVALID_MATCH_RECORD_3),
        format_match_record(INVALID_MATCH_RECORD_4),
        format_match_record(INVALID_MATCH_RECORD_5),
        format_match_record(INVALID_MATCH_RECORD_6),
        format_match_record(INVALID_MATCH_RECORD_7),
        format_match_record(INVALID_MATCH_RECORD_8),
        format_match_record(INVALID_MATCH_RECORD_9),
        INVALID_MATCH_RECORD_10,
    ]


@pytest.fixture
def soccer_team_1():
    return dataclasses.SoccerTeam(
        name="San Jose Earthquakes",
        win_count=1,
        draw_count=1,
        lose_count=1,
    )


@pytest.fixture
def soccer_team_2():
    return dataclasses.SoccerTeam(
        name="Santa Cruz Slugs", win_count=0, draw_count=1, lose_count=0
    )


@pytest.fixture
def soccer_team_3():
    return dataclasses.SoccerTeam(
        name="Capitola Seahorses", win_count=0, draw_count=0, lose_count=1
    )


@pytest.fixture
def soccer_team_4():
    return dataclasses.SoccerTeam(
        name="Aptos FC", win_count=1, draw_count=0, lose_count=0
    )


@pytest.fixture
def matchday_1(soccer_team_1, soccer_team_2):
    return dataclasses.Matchday(count=1, teams=[soccer_team_1, soccer_team_2])


@pytest.fixture
def matchday_2(soccer_team_3, soccer_team_4):
    return dataclasses.Matchday(count=2, teams=[soccer_team_4, soccer_team_3])
