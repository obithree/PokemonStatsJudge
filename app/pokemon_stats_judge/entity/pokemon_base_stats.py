"""Entity of PokemonBaseStats"""
import dataclasses
from pokemon_stats_judge.entity.error import InvalidArgumentTypeError


@dataclasses.dataclass(frozen=True)
class PokemonBaseStats:
    """ポケモンの種族値
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
