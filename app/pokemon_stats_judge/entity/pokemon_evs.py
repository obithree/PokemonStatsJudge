import dataclasses
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValueException
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValuesException


@dataclasses.dataclass(frozen=True)
class PokemonEffortValues:
    hp: int
    phys_atk: int
    phys_def: int
    spcl_atk: int
    spcl_def: int
    speed: int

    def __post_init__(self) -> None:
        self.is_valid()

    def get_dict(self) -> dict:
        return dataclasses.asdict(self)

    def is_valid(self) -> None:
        evs_dict = self.get_dict()
        for arg_name, expected_arg_type in self.__annotations__.items():
            if not isinstance(evs_dict[arg_name], expected_arg_type):
                raise InvalidArgumentTypeException(arg_name, type(evs_dict[arg_name]), expected_arg_type)
        for stat, effort_value in evs_dict.items():
            self._ev_check(stat, effort_value)
        self._ev_sum_check(evs_dict)

    @classmethod
    def _ev_check(cls, stat: str, effort_value: int) -> None:
        if effort_value > 255 or effort_value < 0:
            raise InvalidEffortValueException(stat, effort_value)

    @classmethod
    def _ev_sum_check(cls, evs_dict: list) -> None:
        evs_sum = sum(evs_dict.values())
        print(evs_sum)
        if evs_sum > 510 or evs_sum < 0:
            raise InvalidEffortValuesException(evs_sum)
