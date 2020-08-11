import unittest
import pytest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidIndividualValueException


class TestPokemonIndividualValues(object):
    def test_create_ivs(self, test_ivs):
        ivs = PokemonIndividualValues(
            hp=test_ivs['hp'],
            phys_atk=test_ivs['phys_atk'],
            phys_def=test_ivs['phys_def'],
            spcl_atk=test_ivs['spcl_atk'],
            spcl_def=test_ivs['spcl_def'],
            speed=test_ivs['speed']
        )
        assert ivs.hp is 23

    def test_schema_ivs_value(self, test_evs):
        with pytest.raises(InvalidIndividualValueException):
            PokemonIndividualValues(
                hp=[7,8],
                phys_atk=[7,8],
                phys_def=[7,8],
                spcl_atk=[7,8],
                spcl_def=[7,8],
                speed=[39]
            )
