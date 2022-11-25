import pytest

from matchday.constants import MATCH_RECORDS
from matchday.service_objects import MatchRecordParser

MATCH_RECORD_1 = 'San Jose Earthquakes 3, Santa Cruz Slugs 3\n'
MATCH_RECORD_2 = 'Capitola Seahorses 1, Aptos FC 0'
MATCH_RECORD_3 = 'Felton Lumberjacks 0, Monterey United 2'

INVALID_MATCH_RECORD_1 = ''
INVALID_MATCH_RECORD_2 = '0'
INVALID_MATCH_RECORD_3 = 'Felton'
INVALID_MATCH_RECORD_4 = 'Felton Lumberjacks'
INVALID_MATCH_RECORD_5 = 'Felton Lumberjacks, Aptos FC 0'
INVALID_MATCH_RECORD_6 = 'Aptos FC 0, '
INVALID_MATCH_RECORD_7 = 'Aptos FC 0, 0'
INVALID_MATCH_RECORD_8 = 'Aptos FC 0, Felton'
INVALID_MATCH_RECORD_9 = 'Aptos FC 0, 0 Felton'
INVALID_MATCH_RECORD_10 = 'Felton Lumberjacks 0,Monterey United 2'

def test_match_record_parser_1():
    parser = MatchRecordParser(MATCH_RECORD_1).run()
    assert parser.match_record == MATCH_RECORD_1
    assert parser.is_valid
    assert parser.team_1_name == 'San Jose Earthquakes'
    assert parser.team_1_goal_count == 3
    assert parser.team_1_match_points == 1 
    assert parser.team_2_name == 'Santa Cruz Slugs'
    assert parser.team_2_goal_count == 3
    assert parser.team_2_match_points == 1

def test_match_record_parser_2():
    parser = MatchRecordParser(MATCH_RECORD_2).run()
    assert parser.match_record == MATCH_RECORD_2
    assert parser.is_valid
    assert parser.team_1_name == 'Capitola Seahorses'
    assert parser.team_1_goal_count == 1
    assert parser.team_1_match_points == 3 
    assert parser.team_2_name == 'Aptos FC'
    assert parser.team_2_goal_count == 0
    assert parser.team_2_match_points == 0

def test_match_record_parser_3():
    parser = MatchRecordParser(MATCH_RECORD_3).run()
    assert parser.match_record == MATCH_RECORD_3
    assert parser.is_valid
    assert parser.team_1_name == 'Felton Lumberjacks'
    assert parser.team_1_goal_count == 0
    assert parser.team_1_match_points == 0 
    assert parser.team_2_name == 'Monterey United'
    assert parser.team_2_goal_count == 2
    assert parser.team_2_match_points == 3

def test_match_record_parser_incomplete_match_record():
    parser_1 = MatchRecordParser(INVALID_MATCH_RECORD_1).run()
    assert parser_1.match_record == INVALID_MATCH_RECORD_1
    assert not parser_1.is_valid
    assert parser_1.team_1_name is None
    assert parser_1.team_1_goal_count is None
    assert parser_1.team_1_match_points is None
    assert parser_1.team_2_name is None
    assert parser_1.team_2_goal_count is None
    assert parser_1.team_2_match_points is None

    parser_2 = MatchRecordParser(INVALID_MATCH_RECORD_2).run()
    assert parser_2.match_record == INVALID_MATCH_RECORD_2
    assert not parser_2.is_valid
    assert parser_2.team_1_name is None
    assert parser_2.team_1_goal_count is None
    assert parser_2.team_1_match_points is None
    assert parser_2.team_2_name is None
    assert parser_2.team_2_goal_count is None
    assert parser_2.team_2_match_points is None

    parser_3 = MatchRecordParser(INVALID_MATCH_RECORD_3).run()
    assert parser_3.match_record == INVALID_MATCH_RECORD_3
    assert not parser_3.is_valid
    assert parser_3.team_1_name is None
    assert parser_3.team_1_goal_count is None
    assert parser_3.team_1_match_points is None
    assert parser_3.team_2_name is None
    assert parser_3.team_2_goal_count is None
    assert parser_3.team_2_match_points is None

    parser_4 = MatchRecordParser(INVALID_MATCH_RECORD_4).run()
    assert parser_4.match_record == INVALID_MATCH_RECORD_4
    assert not parser_4.is_valid
    assert parser_4.team_1_name is None
    assert parser_4.team_1_goal_count is None
    assert parser_4.team_1_match_points is None
    assert parser_4.team_2_name is None
    assert parser_4.team_2_goal_count is None
    assert parser_4.team_2_match_points is None

    parser_5 = MatchRecordParser(INVALID_MATCH_RECORD_5).run()
    assert parser_5.match_record == INVALID_MATCH_RECORD_5
    assert not parser_5.is_valid
    assert parser_5.team_1_name is None
    assert parser_5.team_1_goal_count is None
    assert parser_5.team_1_match_points is None
    assert parser_5.team_2_name is None
    assert parser_5.team_2_goal_count is None
    assert parser_5.team_2_match_points is None

    parser_6 = MatchRecordParser(INVALID_MATCH_RECORD_6).run()
    assert parser_6.match_record == INVALID_MATCH_RECORD_6
    assert not parser_6.is_valid
    assert parser_6.team_1_name is None
    assert parser_6.team_1_goal_count is None
    assert parser_6.team_1_match_points is None
    assert parser_6.team_2_name is None
    assert parser_6.team_2_goal_count is None
    assert parser_6.team_2_match_points is None

    parser_7 = MatchRecordParser(INVALID_MATCH_RECORD_7).run()
    assert parser_7.match_record == INVALID_MATCH_RECORD_7
    assert not parser_7.is_valid
    assert parser_7.team_1_name is None
    assert parser_7.team_1_goal_count is None
    assert parser_7.team_1_match_points is None
    assert parser_7.team_2_name is None
    assert parser_7.team_2_goal_count is None
    assert parser_7.team_2_match_points is None

    parser_8 = MatchRecordParser(INVALID_MATCH_RECORD_8).run()
    assert parser_8.match_record == INVALID_MATCH_RECORD_8
    assert not parser_8.is_valid
    assert parser_8.team_1_name is None
    assert parser_8.team_1_goal_count is None
    assert parser_8.team_1_match_points is None
    assert parser_8.team_2_name is None
    assert parser_8.team_2_goal_count is None
    assert parser_8.team_2_match_points is None

    parser_9 = MatchRecordParser(INVALID_MATCH_RECORD_9).run()
    assert parser_9.match_record == INVALID_MATCH_RECORD_9
    assert not parser_9.is_valid
    assert parser_9.team_1_name is None
    assert parser_9.team_1_goal_count is None
    assert parser_9.team_1_match_points is None
    assert parser_9.team_2_name is None
    assert parser_9.team_2_goal_count is None
    assert parser_9.team_2_match_points is None

    parser_10 = MatchRecordParser(INVALID_MATCH_RECORD_10).run()
    assert parser_10.match_record == INVALID_MATCH_RECORD_10
    assert not parser_10.is_valid
    assert parser_10.team_1_name is None
    assert parser_10.team_1_goal_count is None
    assert parser_10.team_1_match_points is None
    assert parser_10.team_2_name is None
    assert parser_10.team_2_goal_count is None
    assert parser_10.team_2_match_points is None
