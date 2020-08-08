import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonBaseStats:
    pokemon_name: str
    base_hp: int
    base_atk: int
    base_def: int
    base_spcl_atk: int
    base_spcl_def: int
    base_speed: int
