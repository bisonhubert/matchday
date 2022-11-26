import pytest

from matchday.dataclasses import Matchday
from matchday.service_objects import MatchRecordParser, MatchdayInterface


def test_matchday_interface_1(match_records_1):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.count == 1
    assert interface.matchday.name == 'Matchday 1'
    for record in match_records_1:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )


def test_matchday_interface_2(match_records_2):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.count == 1
    assert interface.matchday.name == 'Matchday 1'
    for record in match_records_2:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )


def test_matchday_interface_multiple_days(multiple_matchday_match_records):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.count == 1
    assert interface.matchday.name == 'Matchday 1'
    for record in multiple_matchday_match_records:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.count == 2
    assert interface.matchday.name == 'Matchday 2'
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
