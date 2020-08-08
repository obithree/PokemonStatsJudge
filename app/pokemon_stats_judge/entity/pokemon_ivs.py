import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonIndividualValues:
    ivs_hp: int
    ivs_atk: int
    ivs_def: int
    ivs_spcl_atk: int
    ivs_spcl_def: int
    ivs_speed: int
