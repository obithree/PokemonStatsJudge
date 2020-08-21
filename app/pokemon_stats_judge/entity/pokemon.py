"""Entity of Pokemon"""
import dataclasses
import os
import math
import json
from .error import InvalidArgumentTypeError
from .pokemon_base_stats import PokemonBaseStats
from .pokemon_evs import PokemonEffortValues
from .pokemon_ivs import PokemonIndividualValues


@dataclasses.dataclass(frozen=True)
class Pokemon:
    """ポケモンのエンティティ\n
        能力値の実値とレベル、性格を含み、個体値、努力値、種族値オブジェクトを持つ。
    """
    pokemon_name: str
    pokemon_level: int
    pokemon_nature: str
    pokemon_stat_hp: int
    pokemon_stat_phys_atk: int
    pokemon_stat_phys_def: int
    pokemon_stat_spcl_atk: int
    pokemon_stat_spcl_def: int
    pokemon_stat_speed: int
    pokemon_base_stats: PokemonBaseStats = None
    pokemon_ivs: PokemonIndividualValues = None
    pokemon_evs: PokemonEffortValues = None

    def __post_init__(self) -> None:
        """型チェックとスキーマチェックのためにis_valid()を実行する。
        """
        self.is_valid()

    def get_dict(self) -> dict:
        """自身をdict型に変換したものを返す。
        """
        return dataclasses.asdict(self)

    def is_valid(self) -> None:
        """型チェック、スキーマチェックを実行する。
        """
        pokemon_dict = vars(self)
        for arg_name, expected_arg_type in self.__annotations__.items(): # pylint: disable=no-member
            # 種族値、個体値、努力値は型がNoneの場合でもTrueを返す。
            # Todo: もっと賢い方法に修正する。 # pylint: disable=fixme
            if arg_name in ('pokemon_base_stats', 'pokemon_ivs', 'pokemon_evs'):
                arg_type_is_valid = (
                    (isinstance(pokemon_dict[arg_name], expected_arg_type))
                    or (pokemon_dict[arg_name] is None)
                )
            else:
                arg_type_is_valid = isinstance(pokemon_dict[arg_name], expected_arg_type)
            if not arg_type_is_valid:
                raise InvalidArgumentTypeError(
                    arg_name,
                    type(pokemon_dict[arg_name]),
                    expected_arg_type
                )

    def _get_pokemon_stat_dict(self) -> dict:
        """ポケモンの能力値のみのdictを返す。
        """
        pokemon_stat_dict = {
            "hp": self.pokemon_stat_hp,
            "phys_atk": self.pokemon_stat_phys_atk,
            "phys_def": self.pokemon_stat_phys_def,
            "spcl_atk": self.pokemon_stat_spcl_atk,
            "spcl_def": self.pokemon_stat_spcl_def,
            "speed": self.pokemon_stat_speed
        }
        return pokemon_stat_dict

    def get_pokemon_by_replaced_base_stats(self, base_stats: PokemonBaseStats) -> 'Pokemon':
        """種族値を入れた自身を返す。
        """
        update_pokemon = dataclasses.replace(self, pokemon_base_stats=base_stats)
        return update_pokemon

    def get_pokemon_by_estimated_ivs_and_evs(self) -> 'Pokemon':
        """個体値と努力値を"_estimate_ivs_and_evs()"で推測する。\n
        もし種族値が空なら、未変更の自身を返す。
        """
        if not self.pokemon_base_stats:
            return self
        if (not self.pokemon_ivs) and (not self.pokemon_evs):
            estimate_ivs_dict, estimate_evs_dict = self._estimate_ivs_and_evs()
            pokemon_ivs = PokemonIndividualValues(**estimate_ivs_dict)
            pokemon_evs = PokemonEffortValues(**estimate_evs_dict)
            update_pokemon = dataclasses.replace(
                self, pokemon_ivs=pokemon_ivs,
                pokemon_evs=pokemon_evs
            )
        return update_pokemon

    def _estimate_ivs_and_evs(self) -> (dict, dict):
        """種族値と実値から個体値と努力値を推測する。\n
        推測した結果をdictで返す。このdictは個体値と努力値の引数として使用できる。
        """
        pokemon_stat_dict = self._get_pokemon_stat_dict()
        base_stat_dict = self.pokemon_base_stats.get_dict()
        nature_change_dict = self._get_nature_change_dict(self.pokemon_nature)
        stats_list = pokemon_stat_dict.keys()
        estimate_ivs_dict = {}
        estimate_evs_dict = {}
        for stat_name in stats_list:
            # 推測時に計算式がHPとその他で違うため、それのフラグを作成
            estimate_hp = stat_name == "hp"
            # 個体値の推測
            estimate_ivs = self._estimate_stat_ivs(
                self.pokemon_level,
                nature_change_dict[stat_name],
                pokemon_stat_dict[stat_name],
                base_stat_dict[stat_name],
                evs_int=0,
                estimate_hp=estimate_hp
            )
            # 努力値の推測
            # 個体値リストの一番大きな数字が31より大きい場合、個体値を31として推測する。それ以外は0とする。
            if estimate_ivs[-1] > 31:
                estimate_ivs = [31]
                estimate_evs = self._estimate_stat_evs(
                    self.pokemon_level,
                    nature_change_dict[stat_name],
                    pokemon_stat_dict[stat_name],
                    base_stat_dict[stat_name],
                    ivs_int=31,
                    estimate_hp=estimate_hp
                )
            else:
                estimate_evs = 0
            estimate_ivs_dict[stat_name] = estimate_ivs
            estimate_evs_dict[stat_name] = estimate_evs
        return estimate_ivs_dict, estimate_evs_dict

    @classmethod
    def _get_nature_change_dict(cls, pokemon_nature: str) -> dict:
        """性格による能力値の上昇下降の割合のdictを取得する。
        このファイルと同じパスに存在する"nature_change.json"を読み込む。
        """
        nature_change_json_path = f'{os.path.dirname(__file__)}/nature_change.json'
        with open(nature_change_json_path, encoding="utf-8") as nature_change_json:
            nature_change_dict = json.load(nature_change_json)
            return nature_change_dict[pokemon_nature]

    @classmethod
    def _estimate_stat_ivs(cls,
                           level: int,
                           nature_change: float,
                           pokemon_stat: int,
                           base_stat: int,
                           evs_int: int = 0,
                           estimate_hp: bool = False) -> list:
        """努力値を0として扱い、個体値を計算する。\n
        仮に努力値が振られて個体値が31を超えている場合でも、その値を返す。\n
        属性：
              level: ポケモンのレベル
              nature_change: ポケモンの性格による能力倍率
              pokemon_stat: ポケモンの実値
              base_stat: ポケモンの種族値
              evs_int: ポケモンの努力値
              estimate_hp: HPを推定するかどうか。HPの場合は計算式が異なるのでその判定のための引数。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_ivs_list = []
        # 0から31の数字で総当りを行う。切り捨てで一致したものをlistにいれる。
        for estimate_ivs_i in range(32):
            estimate_pokemon_stat = (
                (
                    (base_stat * 2 + estimate_ivs_i + (evs_int / 4)) * level / 100 + stat_change
                ) * nature_change
            )
            if pokemon_stat == int(estimate_pokemon_stat):
                estimate_ivs_list.append(estimate_ivs_i)
        # listが空で、ivsを直接計算した時、31を超えていた場合、推定値をlistに入れる。これは努力値を振っている印
        if not estimate_ivs_list:
            estimate_ivs = (
                (100 * (pokemon_stat / nature_change - stat_change) / level) - (base_stat * 2) - (evs_int / 4)
            )
            estimate_ivs_list.append(estimate_ivs)
        return estimate_ivs_list

    @classmethod
    def _estimate_stat_evs(cls,
                           level: int,
                           nature_change: float,
                           pokemon_stat: int,
                           base_stat: int,
                           ivs_int: int,
                           estimate_hp=False) -> int:
        """実値、個体値、種族値から努力値を計算する。
        属性：
              level: ポケモンのレベル
              nature_change: ポケモンの性格による能力倍率
              pokemon_stat: ポケモンの実値
              base_stat: ポケモンの種族値
              ivs_int: ポケモンの個体値
              estimate_hp: HPを推定するかどうか。HPの場合は計算式が異なるのでその判定のための引数。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_evs = (
            4 * (math.ceil(100 * (pokemon_stat / nature_change - stat_change) / level) - (base_stat * 2) - ivs_int)
        )
        return int(estimate_evs)
