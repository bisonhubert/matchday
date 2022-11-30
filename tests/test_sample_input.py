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
    for indx, record in enumerate(sample_input):
        is_stream_done = indx + 1 == len(sample_input)
        parser = MatchRecordParser(record).run()
        interface.run(parser.get_teams(), is_stream_done)
    assert interface.matchday.name == "Matchday 4"
    assert interface.matchday.count == 4
    assert len(interface.matchday.teams) == 6
    assert len([team.name for team in interface.matchday.teams]) == len(
        set([team.name for team in interface.matchday.teams])
    )
    report = interface.matchday.print_report()
    expected_output = get_sample_output()
    league_report = interface.league.get_report(use_newlines=True)
    assert len(expected_output) == len(league_report)
    assert league_report == expected_output
