"""Entity of EffortValues"""
import dataclasses
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeError
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValueError
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValuesError


@dataclasses.dataclass(frozen=True)
class PokemonEffortValues:
    """ポケモンの努力値
    """
    hp: int
    phys_atk: int
    phys_def: int
    spcl_atk: int
    spcl_def: int
    speed: int

    def __post_init__(self) -> None:
        """初期化時に型チェックとスキーマチェックのためにis_valid()を実行する。
        """
        self.is_valid()

    def get_dict(self) -> dict:
        """自身をdict型に変換したものを返す。
        """
        return dataclasses.asdict(self)

    def is_valid(self) -> None:
        """型チェック、スキーマチェックを実行する。
        """
        evs_dict = self.get_dict()
        for arg_name, expected_arg_type in self.__annotations__.items(): # pylint: disable=no-member
            if not isinstance(evs_dict[arg_name], expected_arg_type):
                raise InvalidArgumentTypeError(
                    arg_name,
                    type(evs_dict[arg_name]),
                    expected_arg_type
                )
        for stat, effort_value in evs_dict.items():
            self._ev_check(stat, effort_value)
        self._ev_sum_check(evs_dict)

    @classmethod
    def _ev_check(cls, stat: str, effort_value: int) -> None:
        if effort_value > 255 or effort_value < 0:
            raise InvalidEffortValueError(stat, effort_value)

    @classmethod
    def _ev_sum_check(cls, evs_dict: list) -> None:
        evs_sum = sum(evs_dict.values())
        if evs_sum > 510 or evs_sum < 0:
            raise InvalidEffortValuesError(evs_sum)
