from typing import List, Set, Type

from matchday.dataclasses import Matchday, SoccerTeam

class League:

    def __init__(self) -> None: 
        self.teams: Set[Type[SoccerTeam]] = None
        self.matchdays: Set[Type[Matchday]] = None

    def add_match(self, match_record: str) -> None:
        pass

    def report(self) -> List[str]:
        if self.matchdays is None:
            return None
        return [matchday.report for matchday in self.matchdays]

    def __repr__(self) -> None:
        return f'League(teams={self.teams}, matchdays={self.matchdays})'
