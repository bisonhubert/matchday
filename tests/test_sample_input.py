import pytest
import os

from matchday.service_objects import MatchRecordParser, MatchdayInterface


def test_sample_input():
    def get_sample_input(match_records=None):
        file_dir = os.path.dirname(os.path.realpath("__file__"))
        rel_path = "tests/mock_data/sample-input.txt"
        filepath = os.path.join(file_dir, rel_path)
        file = open(filepath)
        match_records = file.readlines()
        file.close()
        return match_records

    def get_sample_output(matchdays=None):
        file_dir = os.path.dirname(os.path.realpath("__file__"))
        rel_path = "tests/mock_data/expected-output.txt"
        filepath = os.path.join(file_dir, rel_path)
        file = open(filepath)
        matchdays = file.readlines()
        file.close()
        return matchdays

    interface = MatchdayInterface()
    sample_input = get_sample_input()
    for record in sample_input:
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams(), parser.is_stream_done)
    assert interface.matchday.name == "Matchday 4"
    assert interface.matchday.count == 4
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report()
    # # test that print() gets called when you run print_report()
    expected_output = get_sample_output()
    league_report = interface.league.get_report()
    # todobison
    ## add newlines between matchdays
    ## the last groups of teams isn't being added to a matchday
    assert len(expected_output) == len(league_report)
    assert league_report == expected_output
