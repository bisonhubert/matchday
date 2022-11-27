import pytest

from matchday.constants import MATCH_RECORDS, MATCHDAY_RECORDS
from matchday.dataclasses import League


def test_initialize_league():
    league = League()
    assert league.matchdays is None
    assert repr(league) == "League(matchdays=None, team_count=None)"
    assert league.prev_matchday is None
    # todobison league.add_matchday()
