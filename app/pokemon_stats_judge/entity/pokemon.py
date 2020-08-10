import dataclasses
import os
import math
import json
from .pokemon_base_stats import PokemonBaseStats
from .pokemon_evs import PokemonEffortValues
from .pokemon_ivs import PokemonIndividualValues


@dataclasses.dataclass(frozen=True)
class Pokemon:
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

    def _create_pokemon_stat_dict(self):
        pokemon_stat_dict = {
            "hp": self.pokemon_stat_hp,
            "phys_atk": self.pokemon_stat_phys_atk,
            "phys_def": self.pokemon_stat_phys_def,
            "spcl_atk": self.pokemon_stat_spcl_atk,
            "spcl_def": self.pokemon_stat_spcl_def,
            "speed": self.pokemon_stat_speed
        }
        return pokemon_stat_dict

    def is_updated_by_replacing_base_stats(self, base_stats:PokemonBaseStats):
        update_pokemon = dataclasses.replace(self, pokemon_base_stats=base_stats)
        return update_pokemon

    def is_updated_by_estimating_ivs_and_evs(self):
        if not self.pokemon_base_stats:
            return self
        if not self.pokemon_ivs and not self.pokemon_evs:
            estimate_ivs_dict, estimate_evs_dict = self._estimate_ivs_and_evs()
            pokemon_ivs = PokemonIndividualValues(**estimate_ivs_dict)
            pokemon_evs = PokemonEffortValues(**estimate_evs_dict)
            update_pokemon = dataclasses.replace(self, pokemon_ivs=pokemon_ivs, pokemon_evs=pokemon_evs)
            return update_pokemon

    def _estimate_ivs_and_evs(self):
        pokemon_stat_dict = self._create_pokemon_stat_dict()
        base_stat_dict = dataclasses.asdict(self.pokemon_base_stats)
        nature_change_dict = self._create_nature_change_dict(self.pokemon_nature)
        stats_list = ["hp","phys_atk","phys_def","spcl_atk","spcl_def","speed"]
        estimate_ivs_dict = {}
        estimate_evs_dict = {}
        for stat in stats_list:
            if stat == "hp":
                estimate_hp = True
            else:
                estimate_hp = False

            estimate_ivs = self._estimate_stat_ivs(
                self.pokemon_level,
                nature_change_dict[stat],
                pokemon_stat_dict[stat],
                base_stat_dict[stat],
                evs_int=0,
                estimate_hp=estimate_hp
            )

            if estimate_ivs[0] > 31:
                estimate_ivs = [31]
                estimate_evs = self._estimate_stat_evs(
                    self.pokemon_level,
                    nature_change_dict[stat],
                    pokemon_stat_dict[stat],
                    base_stat_dict[stat],
                    ivs_int=estimate_ivs[0],
                    estimate_hp=estimate_hp
                )
            else:
                estimate_evs = 0
            estimate_ivs_dict[stat] = estimate_ivs
            estimate_evs_dict[stat] = estimate_evs
        return estimate_ivs_dict, estimate_evs_dict

    @classmethod
    def _create_nature_change_dict(cls, pokemon_nature):
        nature_change_json_path = f'{os.path.dirname(__file__)}/nature_change.json'
        with open(nature_change_json_path, encoding="utf-8") as nature_change_json:
            nature_change_dict = json.load(nature_change_json)
            return nature_change_dict[pokemon_nature]

    @classmethod
    def _estimate_stat_ivs(cls, level, nature_change, pokemon_stat, base_stat, evs_int=0, estimate_hp=False):
        """努力値を0として扱い、個体値を計算する。
        仮に努力値が振られて個体値が31を超えている場合でも、その値を返す。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_ivs_list = []
        # 0から31の数字で総当りを行う。切り捨てで一致したものをlistにいれる。
        for estimate_ivs_i in range(32):
            estimate_pokemon_stat = ((base_stat * 2 + estimate_ivs_i + (evs_int / 4)) * level / 100 + stat_change) * nature_change
            if pokemon_stat == int(estimate_pokemon_stat):
                estimate_ivs_list.append(estimate_ivs_i)
        # listが空で、ivsを直接計算した時、31を超えていた場合、推定値をlistに入れる。これは努力値を振っている印
        if not estimate_ivs_list:
            estimate_ivs = ( 100 * ( pokemon_stat / nature_change - stat_change ) / level ) - ( base_stat * 2 ) - ( evs_int / 4 )
            estimate_ivs_list.append(estimate_ivs)
        return estimate_ivs_list

    @classmethod
    def _estimate_stat_evs(cls, level, nature_change, pokemon_stat, base_stat, ivs_int, estimate_hp=False):
        """実値、個体値、種族値から努力値を計算する。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_evs = 4 * ( math.ceil( 100 * ( pokemon_stat / nature_change - stat_change ) / level ) - ( base_stat * 2 ) - ivs_int )
        return int(estimate_evs)
