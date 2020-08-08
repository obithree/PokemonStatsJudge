import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonBaseStats:
    pokemon_name: str
    pokemon_base_hp: int
    pokemon_base_atk: int
    pokemon_base_def: int
    pokemon_base_spcl_atk: int
    pokemon_base_spcl_def: int
    pokemon_base_speed: int

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
