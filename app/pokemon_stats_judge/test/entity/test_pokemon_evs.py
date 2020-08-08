import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues


class TestPokemonEffortValues(object):
    def test_create_evs(self, test_evs):
        evs = PokemonEffortValues(
            evs_hp=test_evs['evs_hp'],
            evs_atk=test_evs['evs_atk'],
            evs_def=test_evs['evs_def'],
            evs_spcl_atk=test_evs['evs_spcl_atk'],
            evs_spcl_def=test_evs['evs_spcl_def'],
            evs_speed=test_evs['evs_speed']
        )
        assert evs.evs_hp is 252
    
    def test_schema_evs(self):
        try:
            evs = PokemonEffortValues(
                evs_hp=252,
                evs_atk=0,
                evs_def=0,
                evs_spcl_atk=252,
                evs_spcl_def=0,
                evs_speed=0
            )
        except EffortValuesError:
            pass

