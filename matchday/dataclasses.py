from __future__ import annotations
from dataclasses import dataclass
from operator import attrgetter
from typing import List, Set, Type


@dataclass(order=True)
class SoccerTeam:
    """
    A record of a soccer team and their performance in the league.

    Attributes
    - name: the name of the team
    - win_count: the number of wins the team has accrued in the league
    - draw_count: the number of draws the team has accrued in the league
    - lose_count: the number of losses the team has accrued in the league

    Properties
    - points: the total points earned by the team
    - matchday_report: the matchday report string for the team
    - record: the W-D-L record for the team
    """

    name: str = None
    win_count: int = 0
    draw_count: int = 0
    lose_count: int = 0

    @property
    def points(self) -> int:
        """
        A win is worth 3 points, a draw is worth 1 point. A loss is worth zero points,
        so it is not included in the calculation.
        """
        return self.win_count * 3 + self.draw_count

    @property
    def matchday_report(self) -> str:
        unit = "pt" if self.points == 1 else "pts"
        return f"{self.name}, {self.points} {unit}"

    @property
    def record(self) -> str:
        return f"{self.win_count}-{self.draw_count}-{self.lose_count}"


@dataclass
class Matchday:
    """
    A record of soccer teams and scores for a day of matches.

    Attributes
    - count: the number of the matchday in a league
    - teams: a collection of SoccerTeam objects, representing teams playing in the matchday

    Properties
    - name: the name of the matchday, including the matchday count

    Private Methods
    - _rank_matchday_teams: sorts teams by points and team name
    - _print_report: iterates through each line in the report and prints it to stdout

    Public Methods
    - find_team: returns a SoccerTeam from the list of teams playing in a matchday
    - get_full_report: returns the matchday name and SoccerTeam report for every team that played
    - print_report: prints the matchday name and top 3 teams of a matchday
    """

    count: int = None
    teams: List[Type[SoccerTeam]] = None

    @property
    def name(self):
        return f"Matchday {self.count}"

    def _rank_matchday_teams(self) -> List[str]:
        """
        Teams are ranked by points, descending. If points are tied, order by team name asc.
        """
        if self.teams is None:
            return None
        teams = sorted(self.teams, key=attrgetter("name"))
        return sorted(teams, key=attrgetter("points"), reverse=True)

    def _print_report(self, report: List[str] = None) -> str:
        if report is None:
            return None
        for report_line in report:
            print(report_line, end="")

    def find_team(self, team_name: str) -> Type[SoccerTeam]:
        if self.teams is None:
            return None
        team = next(
            iter(list(filter(lambda x: x.name == team_name, self.teams)) or []), None
        )
        return team

    def get_full_report(self, use_newlines: bool = False):
        if self.teams is None:
            return [f"{self.name}"]
        if use_newlines:
            return [
                f"{self.name}\n",
                *[
                    f"{report}\n"
                    for report in [
                        f"{team.matchday_report}"
                        for team in self._rank_matchday_teams()
                    ]
                ],
            ]
        return [
            self.name,
            *[f"{team.matchday_report}" for team in self._rank_matchday_teams()],
        ]

    def print_report(self, is_stream_done: bool = False) -> List[str]:
        report = self.get_full_report(use_newlines=True)
        if report is None:
            return None
        if len(report) > 4:
            report = report[:4]
            if not is_stream_done:
                report.append("\n")
        self._print_report(report)
        return report


@dataclass
class League:
    """
    A league is a collection of Matchday objects.

    Attributes
    - matchdays: a collection of Matchday objects
    - team_count: the number of teams in a league

    Properties
    - prev_matchday: the most recent completed matchday in the league

    Public Methods
    - add_matchday: adds a Matchday to the list of matchdays
    - get_team: returns a SoccerTeam from the previous matchday
    - get_report: returns the full report for every Matchday
    """

    matchdays: Set[Type[Matchday]] = None
    team_count: int = None

    @property
    def prev_matchday(self) -> Type[Matchday]:
        if self.matchdays is None:
            return None
        return self.matchdays[-1]

    def add_matchday(self, matchday: Type[Matchday]) -> None:
        if self.matchdays is None:
            self.matchdays = []
        self.matchdays.append(matchday)
        return None

    def get_team(self, team_name: str) -> Type[SoccerTeam]:
        if self.matchdays is None:
            return None
        return self.prev_matchday.find_team(team_name)

    def get_report(self, use_newlines: bool = False) -> List[str]:
        report = []
        for matchday in self.matchdays:
            report = [*report, *matchday.get_full_report(use_newlines=True)[:4], "\n"]
        return report[:-1]  # strip newline at the end
