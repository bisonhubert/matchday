from __future__ import annotations
from typing import List, Type

class MatchRecordParser:
    MATCH_POINT_WIN = 3
    MATCH_POINT_TIE = 1
    MATCH_POINT_LOSS = 0

    def __init__(self, match_record: str) -> None:
        self.match_record = match_record
        self.team_1_name: str = None
        self.team_1_goal_count: int = None
        self.team_1_match_points: int = None
        self.team_2_name: str = None
        self.team_2_goal_count: int = None
        self.team_2_match_points: int = None

    def _split_teams(self) -> List[str]:
        return self.match_record.strip().split(', ') # split on comma + whitespace

    def _get_team_names(self, teams: List[str]) -> str:
        return [' '.join(team.split(' ')[:-1]) for team in teams]

    def _get_team_goal_count(self, teams: List[str]) -> int:
        return [int(team.split(' ')[-1]) for team in teams]

    def _get_match_points(self) -> None:
        TIE, WIN, LOSS = [
            [self.MATCH_POINT_TIE]*2, 
            [self.MATCH_POINT_WIN, self.MATCH_POINT_LOSS],
            [self.MATCH_POINT_LOSS, self.MATCH_POINT_WIN]
        ]
        if self.team_1_goal_count == self.team_2_goal_count:
            return TIE
        elif self.team_1_goal_count > self.team_2_goal_count:
            return WIN
        elif self.team_1_goal_count < self.team_2_goal_count:
            return LOSS

    def _set_attrs(self) -> None:
        teams = self._split_teams()
        self.team_1_name, self.team_2_name = self._get_team_names(teams)
        self.team_1_goal_count, self.team_2_goal_count = self._get_team_goal_count(teams)
        self.team_1_match_points, self.team_2_match_points = self._get_match_points()

    def run(self) -> MatchRecordParser:
        self._set_attrs()
        return self