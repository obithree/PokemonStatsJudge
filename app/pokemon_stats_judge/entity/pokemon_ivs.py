import dataclasses
from typing import List
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidIndividualValueException


@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    hp: List[int]
    phys_atk: List[int]
    phys_def: List[int]
    spcl_atk: List[int]
    spcl_def: List[int]
    speed: List[int]

    def __post_init__(self) -> None:
        self.is_valid()

    def get_dict(self) -> dict:
        return dataclasses.asdict(self)

    def is_valid(self) -> None:
        ivs_dict = self.get_dict()
        for arg_name, expected_arg_type in self.__annotations__.items():
            # Todo: 型チェックを動的になるよう修正
            if not isinstance(ivs_dict[arg_name], list):
                raise InvalidArgumentTypeException(arg_name, type(ivs_dict[arg_name]), list)
        for stat, individual_list in ivs_dict.items():
            self._iv_check(stat, individual_list)

    @classmethod
    def _iv_check(cls, stat: str, individual_list: list) -> None:
        if max(individual_list) > 31 or max(individual_list) < 0:
            raise InvalidIndividualValueException(stat, max(individual_list))
