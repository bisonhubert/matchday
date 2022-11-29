from __future__ import annotations
from typing import Type

from matchday.dataclasses import League, Matchday, SoccerTeam


class MatchdayInterface:
    def __init__(self) -> None:
        self.league = League()
        self.matchday = Matchday(count=1)

    def _initialize_soccer_team(self, team: dict) -> None:
        name = team.get("name")
        win_count = team.get("win_count", 0)
        lose_count = team.get("lose_count", 0)
        draw_count = team.get("draw_count", 0)
        return SoccerTeam(
            name=name, win_count=win_count, lose_count=lose_count, draw_count=draw_count
        )

    def _update_soccer_team(self, team: dict) -> None:
        prev_team_record = self.league.get_team(team.get("name"))
        win_count = team.get("win_count") + prev_team_record.win_count
        lose_count = team.get("lose_count") + prev_team_record.lose_count
        draw_count = team.get("draw_count") + prev_team_record.draw_count
        return SoccerTeam(
            name=team.get("name"),
            win_count=win_count,
            lose_count=lose_count,
            draw_count=draw_count,
        )

    def _end_matchday(self, is_stream_done: bool = False):
        if self.matchday.count == 1:
            self.league.team_count = len(self.matchday.teams)
        self.league.add_matchday(self.matchday)
        self.matchday.print_report(is_stream_done)

    def _handle_new_matchday(self, teams: List[Type[SoccerTeam]]):
        self._end_matchday()
        soccer_teams = [self._update_soccer_team(team) for team in teams]
        self.matchday = Matchday(count=self.matchday.count + 1, teams=soccer_teams)

    def add_team(self, team: dict) -> None:
        if self.matchday.teams is None:
            self.matchday.teams = []
        self.matchday.teams.append(
            SoccerTeam(
                name=team.get("name"),
                win_count=team.get("win_count"),
                lose_count=team.get("lose_count"),
                draw_count=team.get("draw_count"),
            )
        )

    def is_new_matchday(self, teams: List[dict]) -> bool:
        if self.matchday.count == 1:
            team_1, team_2 = teams
            return (
                self.matchday.find_team(team_1.get("name")) is not None
                or self.matchday.find_team(team_2.get("name")) is not None
            )
        else:
            return len(self.matchday.teams) == len(self.league.prev_matchday.teams)

    def run(self, teams: List[dict], is_stream_done: bool) -> MatchdayInterface:
        if is_stream_done:
            if self.matchday.count == 1:
                [self.add_team(team) for team in teams]
                self.league.team_count = len(self.matchday.teams)
            else:
                if teams is not None:
                    soccer_teams = [self._update_soccer_team(team) for team in teams]
                    self.matchday.teams = [*self.matchday.teams, *soccer_teams]
            self._end_matchday(is_stream_done)
        elif self.is_new_matchday(teams):
            self._handle_new_matchday(teams)
        elif self.matchday.count == 1:
            [self.add_team(team) for team in teams]
        else:
            soccer_teams = [self._update_soccer_team(team) for team in teams]
            self.matchday.teams = [*self.matchday.teams, *soccer_teams]
        return self
