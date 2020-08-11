import unittest
import pytest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValueException
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidEffortValuesException


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

    def test_get_dict(self, test_evs):
        evs = PokemonEffortValues(
            hp=test_evs['hp'],
            phys_atk=test_evs['phys_atk'],
            phys_def=test_evs['phys_def'],
            spcl_atk=test_evs['spcl_atk'],
            spcl_def=test_evs['spcl_def'],
            speed=test_evs['speed']
        )
        evs_dict = evs.get_dict()
        assert isinstance(evs_dict, dict)

    def test_schema_evs_value(self, test_evs):
        with pytest.raises(InvalidEffortValueException):
            PokemonEffortValues(
                hp=300,
                phys_atk=test_evs['phys_atk'],
                phys_def=test_evs['phys_def'],
                spcl_atk=test_evs['spcl_atk'],
                spcl_def=test_evs['spcl_def'],
                speed=test_evs['speed']
            )
    def test_schema_evs_values(self, test_evs):
        with pytest.raises(InvalidEffortValuesException):
            PokemonEffortValues(
                hp=252,
                phys_atk=252,
                phys_def=252,
                spcl_atk=252,
                spcl_def=252,
                speed=252
            )
