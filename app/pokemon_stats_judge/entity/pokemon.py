import dataclasses

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
