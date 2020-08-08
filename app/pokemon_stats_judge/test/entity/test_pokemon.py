import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues


class TestPokemon(object):
    """test class of pokemon entity
    """

    def test_create_pokemon(self, test_pokemon_stats, test_base_stats):
        """test pokemon entity create
        """

        pokemon_base_stats = PokemonBaseStats(
            test_base_stats['pokemon_name'],
            test_base_stats['base_hp'],
            test_base_stats['base_atk'],
            test_base_stats['base_def'],
            test_base_stats['base_spcl_atk'],
            test_base_stats['base_spcl_def'],
            test_base_stats['base_speed']
        )

        test_pokemon = Pokemon(
                                test_pokemon_stats['pokemon_name'],
                                test_pokemon_stats['pokemon_stat_level'],
                                test_pokemon_stats['pokemon_nature'],
                                test_pokemon_stats['pokemon_stat_hp'],
                                test_pokemon_stats['pokemon_stat_atk'],
                                test_pokemon_stats['pokemon_stat_def'],
                                test_pokemon_stats['pokemon_stat_spcl_atk'],
                                test_pokemon_stats['pokemon_stat_spcl_def'],
                                test_pokemon_stats['pokemon_stat_speed'],
                                pokemon_base_stats
        ) 
        assert test_pokemon.pokemon_base_stats.pokemon_name == test_pokemon_stats['pokemon_name']
        assert test_pokemon.pokemon_base_stats.base_hp == 62
