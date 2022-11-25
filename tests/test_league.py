import pytest

from matchday.constants import MATCH_RECORDS, MATCHDAY_RECORDS
from matchday.dataclasses import League


def test_initialize_league():
    league = League()
    assert league.teams is None
    assert league.matchdays is None
    assert repr(league) == "League(teams=None, matchdays=None)"


# def test_league_report():
    # league = League()
    # assert league.report() is None
    # for match_record in MATCH_RECORDS:
    #     league.add_match(match_record)
    # assert league.report() == MATCHDAY_RECORDS
