import dataclasses
from typing import List

@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    ivs_hp: List[int]
    ivs_atk: List[int]
    ivs_def: List[int]
    ivs_spcl_atk: List[int]
    ivs_spcl_def: List[int]
    ivs_speed: List[int]
