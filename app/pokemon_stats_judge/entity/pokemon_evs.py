import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonEffortValues:
    hp: int
    phys_atk: int
    phys_def: int
    spcl_atk: int
    spcl_def: int
    speed: int

    def __post_init__(self):
        self._ev_check(self.hp)
        self._ev_check(self.phys_atk)
        self._ev_check(self.phys_def)
        self._ev_check(self.spcl_atk)
        self._ev_check(self.spcl_def)
        self._ev_check(self.speed)

    def _ev_check(self, ev):
        if ev > 255 or ev < 0:
            raise EffortValuesError()
            # TODO: Logger作成
            # raise EffortValuesError()