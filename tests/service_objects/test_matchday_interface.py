import pytest

from matchday.dataclasses import Matchday
from matchday.service_objects import MatchRecordParser, MatchdayInterface


def test_matchday_interface_1(match_record_1):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert interface.matchday.print_report() == ["Matchday 1"]
    # test that print() gets called when you run print_report()
    parser = MatchRecordParser(match_record_1).run()
    interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    assert interface.matchday.teams[0].win_count == 0
    assert interface.matchday.teams[0].lose_count == 0
    assert interface.matchday.teams[0].draw_count == 1
    assert interface.matchday.teams[1].win_count == 0
    assert interface.matchday.teams[1].lose_count == 0
    assert interface.matchday.teams[1].draw_count == 1
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report[0] == "Matchday 1\n"
    assert report[1] == "San Jose Earthquakes, 1 pt\n"
    assert report[2] == "Santa Cruz Slugs, 1 pt"
    assert report == [
        "Matchday 1\n",
        "San Jose Earthquakes, 1 pt\n",
        "Santa Cruz Slugs, 1 pt",
    ]


def test_matchday_interface_2(match_record_2):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert interface.matchday.print_report() == ["Matchday 1"]
    # test that print() gets called when you run print_report()
    parser = MatchRecordParser(match_record_2).run()
    interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    assert interface.matchday.teams[0].win_count == 1
    assert interface.matchday.teams[0].lose_count == 0
    assert interface.matchday.teams[0].draw_count == 0
    assert interface.matchday.teams[0].points == 3
    assert interface.matchday.teams[1].win_count == 0
    assert interface.matchday.teams[1].lose_count == 1
    assert interface.matchday.teams[1].draw_count == 0
    assert interface.matchday.teams[1].points == 0
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report[0] == "Matchday 1\n"
    assert report[1] == "Capitola Seahorses, 3 pts\n"
    assert report[2] == "Aptos FC, 0 pts"
    assert report == [
        "Matchday 1\n",
        "Capitola Seahorses, 3 pts\n",
        "Aptos FC, 0 pts",
    ]


def test_matchday_interface_3(match_record_3):
    interface = MatchdayInterface()
    assert interface.matchday is not None
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert interface.matchday.print_report() == ["Matchday 1"]
    # test that print() gets called when you run print_report()
    parser = MatchRecordParser(match_record_3).run()
    interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 2
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    assert interface.matchday.teams[0].win_count == 0
    assert interface.matchday.teams[0].lose_count == 1
    assert interface.matchday.teams[0].draw_count == 0
    assert interface.matchday.teams[0].points == 0
    assert interface.matchday.teams[1].win_count == 1
    assert interface.matchday.teams[1].lose_count == 0
    assert interface.matchday.teams[1].draw_count == 0
    assert interface.matchday.teams[1].points == 3
    report = interface.matchday.print_report()
    assert len(report) == 3
    assert report[0] == "Matchday 1\n"
    assert report[1] == "Monterey United, 3 pts\n"
    assert report[2] == "Felton Lumberjacks, 0 pts"
    assert report == [
        "Matchday 1\n",
        "Monterey United, 3 pts\n",
        "Felton Lumberjacks, 0 pts",
    ]


def test_matchday_interface_multiple_teams_1(match_records_1):
    interface = MatchdayInterface()
    for record in match_records_1:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report()
    assert len(report) == 4
    assert report[0] == "Matchday 1\n"
    assert report[1] == "Capitola Seahorses, 3 pts\n"
    assert report[2] == "Monterey United, 3 pts\n"
    assert report[3] == "San Jose Earthquakes, 1 pt"
    assert report == [
        "Matchday 1\n",
        "Capitola Seahorses, 3 pts\n",
        "Monterey United, 3 pts\n",
        "San Jose Earthquakes, 1 pt",
    ]


def test_matchday_interface_multiple_teams_2(match_records_2):
    interface = MatchdayInterface()
    for record in match_records_2:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 1"
    assert interface.matchday.count == 1
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report()
    # test that print() gets called when you run print_report()
    assert len(report) == 4
    assert report[0] == "Matchday 1\n"
    assert report[1] == "Aptos FC, 3 pts\n"
    assert report[2] == "Monterey United, 3 pts\n"
    assert report[3] == "Capitola Seahorses, 1 pt"
    assert report == [
        "Matchday 1\n",
        "Aptos FC, 3 pts\n",
        "Monterey United, 3 pts\n",
        "Capitola Seahorses, 1 pt",
    ]


def test_matchday_interface_multiple_days(multiple_matchday_records):
    interface = MatchdayInterface()
    for record in multiple_matchday_records:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams())
    assert interface.matchday.name == "Matchday 2"
    assert interface.matchday.count == 2
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report()
    # test that print() gets called when you run print_report()
    assert len(report) == 4
    # assert report[0] == "Matchday 2\n"
    # assert report[1] == "Monterey United, 6 pts\n"
    # assert report[2] == "Capitola Seahorses, 4 pts\n"
    # assert report[3] == 'Aptos FC, 3 pts'
    # assert report == [
    #     "Matchday 2\n",
    #     "Monterey United, 6 pts\n",
    #     "Capitola Seahorses, 4 pts\n",
    #     'Aptos FC, 3 pts'
    # ]
