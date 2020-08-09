import dataclasses
from typing import List

@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    hp: List[int]
    phys_atk: List[int]
    phys_def: List[int]
    spcl_atk: List[int]
    spcl_def: List[int]
    speed: List[int]
