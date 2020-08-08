import dataclasses


@dataclasses.dataclass(frozen=True)
class PokemonEffortValues:
    evs_hp: int
    evs_atk: int
    evs_def: int
    evs_spcl_atk: int
    evs_spcl_def: int
    evs_speed: int

    def __post_init__(self):
        self._ev_check(self.evs_hp)
        self._ev_check(self.evs_atk)
        self._ev_check(self.evs_def)
        self._ev_check(self.evs_spcl_atk)
        self._ev_check(self.evs_spcl_def)
        self._ev_check(self.evs_speed)

    def _ev_check(self, ev):
        if ev > 255 or ev < 0:
            raise EffortValuesError()
            # TODO: Logger作成
            # raise EffortValuesError()