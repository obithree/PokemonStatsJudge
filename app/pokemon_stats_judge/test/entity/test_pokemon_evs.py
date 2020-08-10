import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues


class TestPokemonEffortValues(object):
    def test_create_evs(self, test_evs):
        evs = PokemonEffortValues(
            hp=test_evs['hp'],
            phys_atk=test_evs['phys_atk'],
            phys_def=test_evs['phys_def'],
            spcl_atk=test_evs['spcl_atk'],
            spcl_def=test_evs['spcl_def'],
            speed=test_evs['speed']
        )
        assert evs.hp is 252
    
    def test_schema_evs(self, test_evs):
        try:
            evs = PokemonEffortValues(
                hp=test_evs['hp'],
                phys_atk=test_evs['phys_atk'],
                phys_def=test_evs['phys_def'],
                spcl_atk=test_evs['spcl_atk'],
                spcl_def=test_evs['spcl_def'],
                speed=test_evs['speed']
            )
        except EffortValuesError:
            pass

