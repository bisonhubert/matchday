from dataclasses import dataclass
from typing import List

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
