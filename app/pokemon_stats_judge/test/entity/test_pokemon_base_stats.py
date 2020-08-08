import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues


class TestPokemonBaseStats(object):
    def test_create_base_stats(self, test_base_stats):
        pokemon_base_stats = PokemonBaseStats(
            test_base_stats['pokemon_name'],
            test_base_stats['base_hp'],
            test_base_stats['base_atk'],
            test_base_stats['base_def'],
            test_base_stats['base_spcl_atk'],
            test_base_stats['base_spcl_def'],
            test_base_stats['base_speed']
        )
        assert pokemon_base_stats.pokemon_name == 'ヒノヤコマ' 
