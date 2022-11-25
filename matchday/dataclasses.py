from dataclasses import dataclass
from typing import List, Set, Type


@dataclass
class SoccerMatch:
    """
    Class for recording a soccer match
    """

    original_record: str


@dataclass
class SoccerTeam:
    points: int
    name: str
    record: str


@dataclass
class Matchday:

    # def report(self) -> List[str, ...]:
    def report(self) -> None:
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
