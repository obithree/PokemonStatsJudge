import dataclasses
from .pokemon_base_stats import PokemonBaseStats
from .pokemon_evs import PokemonEffortValues
from .pokemon_ivs import PokemonIndividualValues


@dataclasses.dataclass(frozen=True)
class Pokemon:
    pokemon_name: str
    pokemon_stat_level: int
    pokemon_nature: str
    pokemon_stat_hp: int
    pokemon_stat_atk: int
    pokemon_stat_def: int
    pokemon_stat_spcl_atk: int
    pokemon_stat_spcl_def: int
    pokemon_stat_speed: int
    pokemon_base_stats: PokemonBaseStats = None
    pokemon_ivs: PokemonIndividualValues = None
    pokemon_evs: PokemonEffortValues = None

    def is_updated_by_replacing_base_stats(self, base_stats:PokemonBaseStats):
        update_pokemon = dataclasses.replace(self, pokemon_base_stats=base_stats)
        return update_pokemon

    def _estimate_ivs_and_evs(self):
        if self.pokemon_base_stats is None:
            return
        if self.pokemon_ivs is not None and self.pokemon_evs is not None:
            return

    def _estimate_stat_all_ivs(self):
        pass

    @classmethod
    def _estimate_stat_ivs(cls, level, nature_change, pokemon_stat, base_stat, evs=0, estimate_hp=False):
        """努力値を0として扱い、個体値を計算する。
        仮に努力値が振られて個体値が31を超えた場合、個体値は31とする。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_ivs = ( 100 * ( pokemon_stat / nature_change - stat_change ) / level ) - ( base_stat * 2 ) - ( evs / 4 )
        if estimate_ivs > 31:
            estimate_ivs = 31
        return estimate_ivs

    @classmethod
    def _estimate_stat_evs(cls, level, nature_change, pokemon_stat, base_stat, ivs, estimate_hp=False):
        """実値、個体値、種族値から努力値を計算する。
        """
        if estimate_hp:
            stat_change = level + 10
        else:
            stat_change = 5
        estimate_evs = 4 * ( ( 100 * ( pokemon_stat / nature_change - stat_change ) / level ) - ( base_stat * 2 ) - ivs )
        return estimate_evs
