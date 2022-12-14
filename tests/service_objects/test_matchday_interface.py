import pytest
import os

from matchday.service_objects import MatchRecordParser, MatchdayInterface


def test_matchday_interface_init():
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert interface.matchday.print_report() == ["Matchday 1"]


def test_matchday_interface_1(match_record_1):
    parser = MatchRecordParser(match_record_1).run()
    interface = MatchdayInterface()
    interface.run(parser.get_teams(), True)
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert interface.league.team_count == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    team_1, team_2 = interface.matchday.teams
    assert team_1.win_count == 0
    assert team_1.draw_count == 1
    assert team_1.lose_count == 0
    assert team_1.record == "0-1-0"
    assert team_1.points == 1
    assert team_2.win_count == 0
    assert team_2.draw_count == 1
    assert team_2.lose_count == 0
    assert team_2.record == "0-1-0"
    assert team_2.points == 1
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report == [
        "Matchday 1\n",
        "San Jose Earthquakes, 1 pt\n",
        "Santa Cruz Slugs, 1 pt\n",
    ]


def test_matchday_interface_2(match_record_2):
    parser = MatchRecordParser(match_record_2).run()
    interface = MatchdayInterface()
    interface.run(parser.get_teams(), True)
    assert interface.league.team_count == 2
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    team_1, team_2 = interface.matchday.teams
    assert team_1.win_count == 1
    assert team_1.draw_count == 0
    assert team_1.lose_count == 0
    assert team_1.record == "1-0-0"
    assert team_1.points == 3
    assert team_2.win_count == 0
    assert team_2.draw_count == 0
    assert team_2.lose_count == 1
    assert team_2.record == "0-0-1"
    assert team_2.points == 0
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report == [
        "Matchday 1\n",
        "Capitola Seahorses, 3 pts\n",
        "Aptos FC, 0 pts\n",
    ]


def test_matchday_interface_3(match_record_3):
    parser = MatchRecordParser(match_record_3).run()
    interface = MatchdayInterface()
    interface.run(parser.get_teams(), True)
    assert interface.league.team_count == 2
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    team_1, team_2 = interface.matchday.teams
    assert team_1.win_count == 1
    assert team_1.draw_count == 0
    assert team_1.lose_count == 0
    assert team_1.record == "1-0-0"
    assert team_1.points == 3
    assert team_2.win_count == 0
    assert team_2.draw_count == 0
    assert team_2.lose_count == 1
    assert team_2.record == "0-0-1"
    assert team_2.points == 0
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report == [
        "Matchday 1\n",
        "Felton Lumberjacks, 3 pts\n",
        "Monterey United, 0 pts\n",
    ]


def test_matchday_interface_multiple_teams_1(match_records_1):
    is_stream_done = False
    interface = MatchdayInterface()
    for indx, record in enumerate(match_records_1):
        is_stream_done = indx + 1 == len(match_records_1)
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams(), is_stream_done)
    assert interface.league.team_count == 6
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report(is_stream_done)
    assert len(report) == 4
    assert report == [
        "Matchday 1\n",
        "Capitola Seahorses, 3 pts\n",
        "Felton Lumberjacks, 3 pts\n",
        "San Jose Earthquakes, 1 pt\n",
    ]


def test_matchday_interface_multiple_teams_2(match_records_2):
    is_stream_done = False
    interface = MatchdayInterface()
    for indx, record in enumerate(match_records_2):
        is_stream_done = indx + 1 == len(match_records_2)
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams(), is_stream_done)
    assert interface.league.team_count == 6
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report(is_stream_done)
    assert len(report) == 4
    assert report == [
        "Matchday 1\n",
        "Aptos FC, 3 pts\n",
        "Monterey United, 3 pts\n",
        "Capitola Seahorses, 1 pt\n",
    ]


def test_matchday_interface_multiple_days(multiple_matchday_records):
    is_stream_done = False
    interface = MatchdayInterface()
    for indx, record in enumerate(multiple_matchday_records):
        is_stream_done = indx + 1 == len(multiple_matchday_records)
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams(), is_stream_done)
    assert interface.league.team_count == 6
    assert interface.matchday.name == "Matchday 2"
    assert interface.matchday.count == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report(is_stream_done)
    assert len(report) == 4
    assert report == [
        "Matchday 2\n",
        "Capitola Seahorses, 4 pts\n",
        "Aptos FC, 3 pts\n",
        "Felton Lumberjacks, 3 pts\n",
    ]
