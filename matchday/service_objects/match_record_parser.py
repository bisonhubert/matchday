from __future__ import annotations
import re
from typing import List, Type

from matchday.constants import DRAW, LOSE, WIN


class MatchRecordParser:
    """
    This handles the business logic of transforming an input stream of data.

    Attributes
    - match_record: the input string of stream data
    - is_valid: a flag that indicates if the match_record is formatted correctly
    - is_stream_done: a flag that indicates if the stream has finished
    - team_1_name: name of the first team in the match_record
    - team_2_name: name of the second team in the match_record
    - team_1_goal_count: number of goals scored by the first team
    - team_2_goal_count: number of goals scored by the second team
    - team_1_win_count: number of wins earned by the first team
    - team_2_win_count: number of wins earned by the second team
    - team_1_lose_count: number of losses earned by the first team
    - team_2_lose_count: number of losses earned by the second team
    - team_1_draw_count: number of draws earned by the first team
    - team_2_draw_count: number of draws earned by the second team

    Private Methods
    - _split_teams: strips incomming match record and splits it into 2 teams
    - _get_team_names: returns team names from incoming string
    - _get_team_goal_count: returns the number of goals for a team
    - _set_team_record: uses the goal count to determine whether a team won, lost, or tied
    - _set_attrs: executes above methods and sets MatchRecordParser attributes
    - _validate: uses a regex to validate the incoming stream data

    Public Methods
    - get_teams: returns a list of dictionaries, for instantiating a SoccerTeam object
    - run: validates the stream input and sets attributes or returns self
    """

    def __init__(self, match_record: str) -> None:
        self.match_record = match_record
        self.is_valid: bool = False
        self.is_stream_done: bool = False
        self.team_1_name: str = None
        self.team_2_name: str = None
        self.team_1_goal_count: int = None
        self.team_2_goal_count: int = None
        self.team_1_win_count: int = 0
        self.team_2_win_count: int = 0
        self.team_1_lose_count: int = 0
        self.team_2_lose_count: int = 0
        self.team_1_draw_count: int = 0
        self.team_2_draw_count: int = 0

    def _split_teams(self) -> List[str]:
        return self.match_record.strip().split(", ")  # split on comma + whitespace

    def _get_team_names(self, teams: List[str]) -> str:
        return [" ".join(team.split(" ")[:-1]) for team in teams]

    def _get_team_goal_count(self, teams: List[str]) -> int:
        return [int(team.split(" ")[-1]) for team in teams]

    def _set_team_record(self) -> None:
        if self.team_1_goal_count == self.team_2_goal_count:
            self.team_1_draw_count = 1
            self.team_2_draw_count = 1
        elif self.team_1_goal_count > self.team_2_goal_count:
            self.team_1_win_count = 1
            self.team_2_lose_count = 1
        elif self.team_1_goal_count < self.team_2_goal_count:
            self.team_1_lose_count = 1
            self.team_2_win_count = 1

    def _set_attrs(self) -> None:
        teams = self._split_teams()
        self.team_1_name, self.team_2_name = self._get_team_names(teams)
        self.team_1_goal_count, self.team_2_goal_count = self._get_team_goal_count(
            teams
        )
        self._set_team_record()

    def _validate(self) -> bool:
        # regex will match with:
        # >= 1 of any single character in the range a-z or A-Z
        # AND any whitespace character
        # FOLLOWED BY any digit
        # FOLLOWED BY a comma and a single whitespace
        # FOLLOWED BY one or more of any single character in the range a-z or A-Z
        # AND any whitespace character, followed by
        # FOLLOWED BY any digit
        # FOLLOWED BY zero or one of a newline character
        regex = re.compile("([a-zA-Z]+\\s)+\\d,\\s{1}([a-zA-Z]+\\s)+\\d(\\n)?")
        self.is_valid = regex.match(self.match_record) is not None

    def get_teams(self):
        return [
            {
                "name": self.team_1_name,
                "win_count": self.team_1_win_count,
                "lose_count": self.team_1_lose_count,
                "draw_count": self.team_1_draw_count,
            },
            {
                "name": self.team_2_name,
                "win_count": self.team_2_win_count,
                "lose_count": self.team_2_lose_count,
                "draw_count": self.team_2_draw_count,
            },
        ]

    def run(self) -> MatchRecordParser:
        self._validate()
        if self.is_valid:
            self._set_attrs()
        return self
