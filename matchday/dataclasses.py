from __future__ import annotations
from dataclasses import dataclass
from operator import attrgetter
from typing import List, Set, Type


@dataclass(order=True)
class SoccerTeam:
    name: str = None
    win_count: int = None
    draw_count: int = None
    lose_count: int = None

    @property
    def points(self) -> int:
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
    count: int = None
    teams: List[Type[SoccerTeam]] = None

    @property
    def name(self):
        return f"Matchday {self.count}"

    def _rank_matchday_teams(self) -> List[str]:
        """
        Teams are ranked by points, descending. If points are tied, order by team name asc.
        """
        teams = sorted(self.teams, key=attrgetter("name"))
        return sorted(teams, key=attrgetter("points"), reverse=True)

    def _get_matchday_report(self) -> List[str]:
        return [f"{team.matchday_report}" for team in self._rank_matchday_teams()]

    def _print_report(self, report: List[str]) -> str:
        print(report)

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
                f"{self.name}{chr(10)}",
                *[f"{report}{chr(10)}" for report in self._get_matchday_report()],
            ]
        return [self.name, *self._get_matchday_report()]

    def print_report(self) -> List[str]:
        report = self.get_full_report(use_newlines=True)
        if len(report) > 4:
            report = report[:4]
        self._print_report(report)
        return report


@dataclass
class League:
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
        return report[:-1]  # do not include the newline at the end
