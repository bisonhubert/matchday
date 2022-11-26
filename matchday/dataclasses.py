from dataclasses import dataclass
from typing import List, Set, Type


@dataclass(order=True)
class SoccerTeam:
    points: int = None
    name: str = None
    win_count: int = None
    lose_count: int = None
    draw_count: int = None


@dataclass
class Matchday:
    count: int = None
    teams: List[Type[SoccerTeam]] = None

    @property
    def name(self):
        return f'Matchday {self.count}'

    def add_team(self, team: dict) -> None:
        if self.teams is None:
            self.teams = []
        self.teams.append(
            SoccerTeam(points=team.get("match_points"), name=team.get("name"))
        )

    def find_team(self, team_name: str) -> Type[SoccerTeam]:
        if self.teams is None:
            return None
        team = next(
            iter(list(filter(lambda x: x.name == team_name, self.teams)) or []), None
        )
        return team

    def print_report(self) -> List[str]:
        # print("printing matchday report")
        return None


@dataclass
class League:
    teams: Set[Type[SoccerTeam]] = None
    matchdays: Set[Type[Matchday]] = None

    def add_match(self, match_record: str) -> None:
        return None

    def report(self) -> List[str]:
        if self.matchdays is None:
            return None
        return [matchday.report for matchday in self.matchdays]
