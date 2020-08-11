import dataclasses
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException


@dataclasses.dataclass(frozen=True)
class PokemonBaseStats:
    hp: int
    phys_atk: int
    phys_def: int
    spcl_atk: int
    spcl_def: int
    speed: int

    def __post_init__(self):
        self.is_valid()

    def get_dict(self) -> None:
        return dataclasses.asdict(self)

    def is_valid(self) -> None:
        evs_dict = self.get_dict()
        for arg_name, expected_arg_type in self.__annotations__.items():
            if not isinstance(evs_dict[arg_name], expected_arg_type):
                raise InvalidArgumentTypeException(arg_name, type(evs_dict[arg_name]), expected_arg_type)
