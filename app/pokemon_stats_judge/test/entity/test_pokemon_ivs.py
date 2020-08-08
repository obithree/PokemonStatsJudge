import unittest
import pytest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues


class TestPokemonIndividualValues(object):
    def test_create_ivs(self, test_ivs):
        ivs = PokemonIndividualValues(
            ivs_hp=test_ivs['ivs_hp'],
            ivs_atk=test_ivs['ivs_atk'],
            ivs_def=test_ivs['ivs_def'],
            ivs_spcl_atk=test_ivs['ivs_spcl_atk'],
            ivs_spcl_def=test_ivs['ivs_spcl_def'],
            ivs_speed=test_ivs['ivs_speed']
        )
        assert ivs.ivs_hp is 23
    
    def test_schema_ivs(self, test_ivs):
        try:
            ivs = PokemonIndividualValues(
                ivs_hp=test_ivs['ivs_hp'],
                ivs_atk=test_ivs['ivs_atk'],
                ivs_def=test_ivs['ivs_def'],
                ivs_spcl_atk=test_ivs['ivs_spcl_atk'],
                ivs_spcl_def=test_ivs['ivs_spcl_def'],
                ivs_speed=test_ivs['ivs_speed']
            )
        except IndividualValuesError:
            pass
