import dataclasses
from typing import List
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidIndividualValueException


@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    hp: List[int]
    phys_atk: List[int]
    phys_def: List[int]
    spcl_atk: List[int]
    spcl_def: List[int]
    speed: List[int]

    def __post_init__(self):
        ivs_dict = dataclasses.asdict(self)
        print(ivs_dict)
        for stat, individual_list in ivs_dict.items():
            print(f'{stat}: {individual_list}')
            self._iv_check(stat, individual_list)

    @classmethod
    def _iv_check(cls, stat, individual_list):
        if max(individual_list) > 31 or max(individual_list) < 0:
            raise InvalidIndividualValueException(stat, max(individual_list))
