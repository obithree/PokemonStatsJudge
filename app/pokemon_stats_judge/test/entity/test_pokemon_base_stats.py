import pytest
import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException


class TestPokemonBaseStats(object):
    def test_create_base_stats(self, test_base_stats):
        base_stats = PokemonBaseStats(
            test_base_stats['hp'],
            test_base_stats['phys_atk'],
            test_base_stats['phys_def'],
            test_base_stats['spcl_atk'],
            test_base_stats['spcl_def'],
            test_base_stats['speed']
        )
        assert base_stats.hp == 62

    def test_get_dict(self, test_base_stats):
        base_stats = PokemonBaseStats(
            test_base_stats['hp'],
            test_base_stats['phys_atk'],
            test_base_stats['phys_def'],
            test_base_stats['spcl_atk'],
            test_base_stats['spcl_def'],
            test_base_stats['speed']
        )
        base_stats_dict = base_stats.get_dict()
        assert isinstance(base_stats_dict, dict)

    def test_is_valid(self, test_base_stats):
        with pytest.raises(InvalidArgumentTypeException):
            base_stats = PokemonBaseStats(
                [100],
                test_base_stats['phys_atk'],
                test_base_stats['phys_def'],
                test_base_stats['spcl_atk'],
                test_base_stats['spcl_def'],
                test_base_stats['speed']
            )
