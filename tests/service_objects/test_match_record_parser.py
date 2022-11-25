import pytest

from matchday.constants import MATCH_RECORDS
from matchday.service_objects import MatchRecordParser


def test_match_record_parser_1(match_record_1):
    parser = MatchRecordParser(match_record_1).run()
    assert parser.match_record == match_record_1
    assert parser.is_valid
    assert parser.team_1_name == "San Jose Earthquakes"
    assert parser.team_1_goal_count == 3
    assert parser.team_1_match_points == 1
    assert parser.team_2_name == "Santa Cruz Slugs"
    assert parser.team_2_goal_count == 3
    assert parser.team_2_match_points == 1


def test_match_record_parser_2(match_record_2):
    parser = MatchRecordParser(match_record_2).run()
    assert parser.match_record == match_record_2
    assert parser.is_valid
    assert parser.team_1_name == "Capitola Seahorses"
    assert parser.team_1_goal_count == 1
    assert parser.team_1_match_points == 3
    assert parser.team_2_name == "Aptos FC"
    assert parser.team_2_goal_count == 0
    assert parser.team_2_match_points == 0


def test_match_record_parser_3(match_record_3):
    parser = MatchRecordParser(match_record_3).run()
    assert parser.match_record == match_record_3
    assert parser.is_valid
    assert parser.team_1_name == "Felton Lumberjacks"
    assert parser.team_1_goal_count == 0
    assert parser.team_1_match_points == 0
    assert parser.team_2_name == "Monterey United"
    assert parser.team_2_goal_count == 2
    assert parser.team_2_match_points == 3


def test_match_record_parser_incomplete_match_record(invalid_match_records):
    for record in invalid_match_records:
        parser = MatchRecordParser(record).run()
        assert parser.match_record == record
        assert not parser.is_valid
        assert parser.team_1_name is None
        assert parser.team_1_goal_count is None
        assert parser.team_1_match_points is None
        assert parser.team_2_name is None
        assert parser.team_2_goal_count is None
        assert parser.team_2_match_points is None
