from __future__ import annotations
from dataclasses import dataclass
from operator import attrgetter
from typing import List, Set, Type


@dataclass(order=True)
class SoccerTeam:
    name: str = None
    win_count: int = None
    lose_count: int = None
    draw_count: int = None

    @property
    def points(self) -> int:
        return self.win_count * 3 + self.draw_count

    @property
    def matchday_report(self) -> str:
        unit = "pt" if self.points == 1 else "pts"
        return f"{self.name}, {self.points} {unit}"

    def update(self, team: dict) -> SoccerTeam:
        # from operator import itemgetter
        # params = {'a': 1, 'b': 2}
        # a, b = itemgetter('a', 'b')(params)
        self.win_count += team.get("win_count")
        self.lose_count += team.get("lose_count")
        self.draw_count += team.get("draw_count")
        return self


@dataclass
class Matchday:
    count: int = None
    teams: List[Type[SoccerTeam]] = None

    def _rank_matchday_teams(self) -> List[str]:
        """
        Teams are ranked by points, descending. If points are tied, order by team name asc.
        """
        teams = sorted(self.teams, key=attrgetter("name"))
        return sorted(teams, key=attrgetter("points"), reverse=True)

    def _get_full_report(self):
        report = [f"{self.name}\n"]
        if self.teams is None:
            return report
        return [*report, *self.format_ranked_teams()]

    @property
    def name(self):
        return f"Matchday {self.count}"

    def format_ranked_teams(self) -> List[str]:
        return [f"{team.matchday_report}\n" for team in self._rank_matchday_teams()]

    def find_team(self, team_name: str) -> Type[SoccerTeam]:
        if self.teams is None:
            return None
        team = next(
            iter(list(filter(lambda x: x.name == team_name, self.teams)) or []), None
        )
        return team

    def print_report(self) -> List[str]:
        report = self._get_full_report()
        if len(report) > 4:
            report = report[:4]
        report[-1] = report[-1].strip()
        print(report)
        return report


@dataclass
class League:
    matchdays: Set[Type[Matchday]] = None

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
