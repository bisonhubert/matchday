import pytest

from matchday.dataclasses import SoccerTeam


def test_soccer_team_init():
    team = SoccerTeam()
    assert str(team) == "SoccerTeam(name=None, win_count=0, draw_count=0, lose_count=0)"
    assert team.points is 0
    assert team.matchday_report == "None, 0 pts"
    assert team.record == "0-0-0"


def test_soccer_team_1(soccer_team_1):
    assert (
        str(soccer_team_1)
        == "SoccerTeam(name='San Jose Earthquakes', win_count=1, draw_count=1, lose_count=1)"
    )
    assert soccer_team_1.points is 4
    assert soccer_team_1.matchday_report == "San Jose Earthquakes, 4 pts"
    assert soccer_team_1.record == "1-1-1"


def test_soccer_team_2(soccer_team_2):
    assert (
        str(soccer_team_2)
        == "SoccerTeam(name='Santa Cruz Slugs', win_count=0, draw_count=1, lose_count=0)"
    )
    assert soccer_team_2.points is 1
    assert soccer_team_2.matchday_report == "Santa Cruz Slugs, 1 pt"
    assert soccer_team_2.record == "0-1-0"


def test_soccer_team_3(soccer_team_3):
    assert (
        str(soccer_team_3)
        == "SoccerTeam(name='Capitola Seahorses', win_count=0, draw_count=0, lose_count=1)"
    )
    assert soccer_team_3.points is 0
    assert soccer_team_3.matchday_report == "Capitola Seahorses, 0 pts"
    assert soccer_team_3.record == "0-0-1"
