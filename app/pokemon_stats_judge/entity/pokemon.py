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
    pokemon_base_stats: PokemonBaseStats
    #pokemon_ivs: PokemonIndividualValues = dataclasses.field(default_factory=dict)
    #pokemon_evs: PokemonEffortValues = dataclasses.field(default_factory=dict)

    def _update_pokemon_ivs(self):
        pass
