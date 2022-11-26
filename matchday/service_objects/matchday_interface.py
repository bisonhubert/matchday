from __future__ import annotations
from typing import Type

from matchday.dataclasses import League, Matchday, SoccerTeam


class MatchdayInterface:
    def __init__(self) -> None:
        self.league = League()
        self.matchday = Matchday(count=1)

    def _add_teams(self, teams: List[dict]) -> None:
        if self.is_new_matchday(teams):
            self._start_new_matchday(teams)
        else:
            [self.matchday.add_team(team) for team in teams]

    def _get_soccer_team(self, team: dict) -> None:
        name = team.get("name")
        win_count = team.get("win_count", 0)
        lose_count = team.get("lose_count", 0)
        draw_count = team.get("draw_count", 0)
        return SoccerTeam(
            name=name, win_count=win_count, lose_count=lose_count, draw_count=draw_count
        )

    def _start_new_matchday(self, teams: List[Type[SoccerTeam]]):
        self.matchday.print_report()
        teams = [self._get_soccer_team(team) for team in teams]
        self.matchday = Matchday(count=self.matchday.count + 1, teams=teams)

    def is_new_matchday(self, teams: List[dict]) -> bool:
        team_1, team_2 = teams
        return (
            self.matchday.find_team(team_1.get("name")) is not None
            or self.matchday.find_team(team_2.get("name")) is not None
        )

    def run(self, teams: List[dict]) -> MatchdayInterface:
        self._add_teams(teams)
        return self
