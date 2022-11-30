import pytest

from matchday.constants import MATCH_RECORDS, MATCHDAY_RECORDS
from matchday.dataclasses import League, Matchday


def test_initialize_league():
    league = League()
    matchday = Matchday(1)
    assert league.matchdays is None
    assert repr(league) == "League(matchdays=None, team_count=None)"
    assert league.prev_matchday is None
    assert league.add_matchday(matchday) is None
    assert len(league.matchdays) == 1
    assert matchday in league.matchdays
    assert league.get_team("team does not exist") is None
    assert len(league.get_report()) == 1
