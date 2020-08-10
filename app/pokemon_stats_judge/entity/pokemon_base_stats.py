import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonBaseStats:
    hp: int
    phys_atk: int
    phys_def: int
    spcl_atk: int
    spcl_def: int
    speed: int
