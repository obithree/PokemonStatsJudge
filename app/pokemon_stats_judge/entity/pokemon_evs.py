import dataclasses
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

    def __post_init__(self):
        evs_dict = dataclasses.asdict(self)
        for stat, effort_value in evs_dict.items():
            self._ev_check(stat, effort_value)
        self._ev_sum_check(evs_dict)

    def get_dict(self):
        return dataclasses.asdict(self)

    @classmethod
    def _ev_check(cls, stat, effort_value):
        if effort_value > 255 or effort_value < 0:
            raise InvalidEffortValueException(stat, effort_value)

    @classmethod
    def _ev_sum_check(cls, evs_dict):
        evs_sum = sum(evs_dict.values())
        print(evs_sum)
        if evs_sum > 510 or evs_sum < 0:
            raise InvalidEffortValuesException(evs_sum)
