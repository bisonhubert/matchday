import pytest

from matchday.constants import MATCH_RECORDS
from matchday.service_objects import MatchRecordParser

MATCH_RECORD_1 = 'San Jose Earthquakes 3, Santa Cruz Slugs 3\n'
MATCH_RECORD_2 = 'Capitola Seahorses 1, Aptos FC 0'
MATCH_RECORD_3 = 'Felton Lumberjacks 0, Monterey United 2'

def test_match_record_parser_1():
    parser = MatchRecordParser(MATCH_RECORD_1).run()
    assert parser.match_record == MATCH_RECORD_1
    assert parser.team_1_name == 'San Jose Earthquakes'
    assert parser.team_1_goal_count == 3
    assert parser.team_1_match_points == 1 
    assert parser.team_2_name == 'Santa Cruz Slugs'
    assert parser.team_2_goal_count == 3
    assert parser.team_2_match_points == 1

def test_match_record_parser_2():
    parser = MatchRecordParser(MATCH_RECORD_2).run()
    assert parser.match_record == MATCH_RECORD_2
    assert parser.team_1_name == 'Capitola Seahorses'
    assert parser.team_1_goal_count == 1
    assert parser.team_1_match_points == 3 
    assert parser.team_2_name == 'Aptos FC'
    assert parser.team_2_goal_count == 0
    assert parser.team_2_match_points == 0

def test_match_record_parser_3():
    parser = MatchRecordParser(MATCH_RECORD_3).run()
    assert parser.match_record == MATCH_RECORD_3
    assert parser.team_1_name == 'Felton Lumberjacks'
    assert parser.team_1_goal_count == 0
    assert parser.team_1_match_points == 0 
    assert parser.team_2_name == 'Monterey United'
    assert parser.team_2_goal_count == 2
    assert parser.team_2_match_points == 3
