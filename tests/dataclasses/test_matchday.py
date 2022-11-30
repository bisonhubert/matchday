import pytest

from matchday.dataclasses import Matchday


def test_initialize_matchday():
    matchday = Matchday()
    assert str(matchday) == "Matchday(count=None, teams=None)"
    assert matchday.name == "Matchday None"
    assert matchday._rank_matchday_teams() is None
    assert matchday.find_team("") is None
    assert matchday.get_full_report() == ["Matchday None"]
    assert matchday.get_full_report(False) == ["Matchday None"]
    assert matchday.get_full_report(True) == ["Matchday None"]
    assert matchday.print_report() == ["Matchday None"]
    assert matchday.print_report(False) == ["Matchday None"]
    assert matchday.print_report(True) == ["Matchday None"]


def test_matchday_1(matchday_1, soccer_team_1, soccer_team_2):
    assert (
        str(matchday_1)
        == "Matchday(count=1, teams="
        + "["
        + "SoccerTeam(name='San Jose Earthquakes', win_count=1, draw_count=1, lose_count=1), "
        + "SoccerTeam(name='Santa Cruz Slugs', win_count=0, draw_count=1, lose_count=0)"
        + "])"
    )
    assert matchday_1.name == "Matchday 1"
    assert matchday_1._rank_matchday_teams() == [soccer_team_1, soccer_team_2]
    assert matchday_1.find_team("not a team") is None
    assert matchday_1.find_team("San Jose Earthquakes") == soccer_team_1
    assert matchday_1.find_team("Santa Cruz Slugs") == soccer_team_2
    assert matchday_1.get_full_report() == [
        "Matchday 1",
        "San Jose Earthquakes, 4 pts",
        "Santa Cruz Slugs, 1 pt",
    ]
    assert matchday_1.get_full_report(False) == [
        "Matchday 1",
        "San Jose Earthquakes, 4 pts",
        "Santa Cruz Slugs, 1 pt",
    ]
    assert matchday_1.get_full_report(True) == [
        "Matchday 1\n",
        "San Jose Earthquakes, 4 pts\n",
        "Santa Cruz Slugs, 1 pt\n",
    ]
    assert matchday_1.print_report() == [
        "Matchday 1\n",
        "San Jose Earthquakes, 4 pts\n",
        "Santa Cruz Slugs, 1 pt\n",
    ]
    assert matchday_1.print_report(False) == [
        "Matchday 1\n",
        "San Jose Earthquakes, 4 pts\n",
        "Santa Cruz Slugs, 1 pt\n",
    ]
    assert matchday_1.print_report(True) == [
        "Matchday 1\n",
        "San Jose Earthquakes, 4 pts\n",
        "Santa Cruz Slugs, 1 pt\n",
    ]


def test_matchday_2(matchday_2, soccer_team_3, soccer_team_4):
    # soccer_team_3 and soccer_team_4 are added to matchday_2 teams as
    # [soccer_team_4, soccer_team_3] so that the sorted function will reorder the teams
    assert (
        str(matchday_2)
        == "Matchday(count=2, teams="
        + "["
        + "SoccerTeam(name='Aptos FC', win_count=1, draw_count=0, lose_count=0), "
        + "SoccerTeam(name='Capitola Seahorses', win_count=0, draw_count=0, lose_count=1)"
        + "])"
    )
    assert matchday_2.name == "Matchday 2"
    assert matchday_2._rank_matchday_teams() == [soccer_team_4, soccer_team_3]
    assert matchday_2.find_team("not a team") is None
    assert matchday_2.find_team("Aptos FC") == soccer_team_4
    assert matchday_2.find_team("Capitola Seahorses") == soccer_team_3
    assert matchday_2.get_full_report() == [
        "Matchday 2",
        "Aptos FC, 3 pts",
        "Capitola Seahorses, 0 pts",
    ]
    assert matchday_2.get_full_report(False) == [
        "Matchday 2",
        "Aptos FC, 3 pts",
        "Capitola Seahorses, 0 pts",
    ]
    assert matchday_2.get_full_report(True) == [
        "Matchday 2\n",
        "Aptos FC, 3 pts\n",
        "Capitola Seahorses, 0 pts\n",
    ]
    assert matchday_2.print_report() == [
        "Matchday 2\n",
        "Aptos FC, 3 pts\n",
        "Capitola Seahorses, 0 pts\n",
    ]
    assert matchday_2.print_report(False) == [
        "Matchday 2\n",
        "Aptos FC, 3 pts\n",
        "Capitola Seahorses, 0 pts\n",
    ]
    assert matchday_2.print_report(True) == [
        "Matchday 2\n",
        "Aptos FC, 3 pts\n",
        "Capitola Seahorses, 0 pts\n",
    ]
