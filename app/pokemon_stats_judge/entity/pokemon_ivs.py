"""Entity of IndividualValues"""
import dataclasses
from typing import List
from pokemon_stats_judge.entity.error import InvalidArgumentTypeError
from pokemon_stats_judge.entity.error import InvalidIndividualValueError


@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    """ポケモンの個体値
    """
    hp: List[int]
    phys_atk: List[int]
    phys_def: List[int]
    spcl_atk: List[int]
    spcl_def: List[int]
    speed: List[int]

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
        ivs_dict = self.get_dict()
        for arg_name, expected_arg_type in self.__annotations__.items(): # pylint: disable=no-member,unused-variable
            # Todo: 型チェックを動的になるよう修正 # pylint: disable=fixme
            if not isinstance(ivs_dict[arg_name], list):
                raise InvalidArgumentTypeError(
                    arg_name,
                    type(ivs_dict[arg_name]),
                    list
                )
        for stat, individual_list in ivs_dict.items():
            self._iv_check(stat, individual_list)

    @classmethod
    def _iv_check(cls, stat: str, individual_list: list) -> None:
        if max(individual_list) > 31 or max(individual_list) < 0:
            raise InvalidIndividualValueError(stat, max(individual_list))
