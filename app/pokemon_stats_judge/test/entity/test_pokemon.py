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

        test_pokemon = Pokemon(
                                test_pokemon_stats['pokemon_name'],
                                test_pokemon_stats['pokemon_level'],
                                test_pokemon_stats['pokemon_nature'],
                                test_pokemon_stats['pokemon_stat_hp'],
                                test_pokemon_stats['pokemon_stat_phys_atk'],
                                test_pokemon_stats['pokemon_stat_phys_def'],
                                test_pokemon_stats['pokemon_stat_spcl_atk'],
                                test_pokemon_stats['pokemon_stat_spcl_def'],
                                test_pokemon_stats['pokemon_stat_speed'],
        ) 
        assert test_pokemon.pokemon_name == test_pokemon_stats['pokemon_name']

    def test_is_updated_by_replacing_base_stats(self, test_pokemon_stats, test_base_stats, test_evs, test_ivs):
        pokemon_base_stats = PokemonBaseStats(
            test_base_stats['hp'],
            test_base_stats['phys_atk'],
            test_base_stats['phys_def'],
            test_base_stats['spcl_atk'],
            test_base_stats['spcl_def'],
            test_base_stats['speed']
        )

        test_pokemon = Pokemon(
                                test_pokemon_stats['pokemon_name'],
                                test_pokemon_stats['pokemon_level'],
                                test_pokemon_stats['pokemon_nature'],
                                test_pokemon_stats['pokemon_stat_hp'],
                                test_pokemon_stats['pokemon_stat_phys_atk'],
                                test_pokemon_stats['pokemon_stat_phys_def'],
                                test_pokemon_stats['pokemon_stat_spcl_atk'],
                                test_pokemon_stats['pokemon_stat_spcl_def'],
                                test_pokemon_stats['pokemon_stat_speed'],
        ) 
        test_pokemon = test_pokemon.is_updated_by_replacing_base_stats(pokemon_base_stats)
        assert test_pokemon.pokemon_base_stats.hp == test_base_stats['hp']

    def test_is_updated_by_estimating_ivs_and_evs(self, test_pokemon_stats, test_base_stats, test_evs, test_ivs):
        pokemon_base_stats = PokemonBaseStats(
            test_base_stats['hp'],
            test_base_stats['phys_atk'],
            test_base_stats['phys_def'],
            test_base_stats['spcl_atk'],
            test_base_stats['spcl_def'],
            test_base_stats['speed']
        )
        test_pokemon = Pokemon(
                                test_pokemon_stats['pokemon_name'],
                                test_pokemon_stats['pokemon_level'],
                                test_pokemon_stats['pokemon_nature'],
                                test_pokemon_stats['pokemon_stat_hp'],
                                test_pokemon_stats['pokemon_stat_phys_atk'],
                                test_pokemon_stats['pokemon_stat_phys_def'],
                                test_pokemon_stats['pokemon_stat_spcl_atk'],
                                test_pokemon_stats['pokemon_stat_spcl_def'],
                                test_pokemon_stats['pokemon_stat_speed'],
        ) 
        test_pokemon = test_pokemon.is_updated_by_replacing_base_stats(pokemon_base_stats)
        test_pokemon = test_pokemon.is_updated_by_estimating_ivs_and_evs()
        assert test_pokemon.pokemon_ivs.hp == [31]
        assert test_pokemon.pokemon_ivs.phys_def == [5,6]
        assert test_pokemon.pokemon_evs.hp == 220
        assert test_pokemon.pokemon_evs.phys_def == 0
        assert test_pokemon.pokemon_evs.speed == 228

    def test_create_nature_change_dict(self):
        nature_change_dict = Pokemon._create_nature_change_dict('ひかえめ')
        assert nature_change_dict['spcl_atk'] == 1.1

    def test_estimate_stat_ivs(self, test_pokemon_stats, test_base_stats, test_evs, test_ivs):
        estimate_ivs_hp = Pokemon._estimate_stat_ivs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_hp'],
            base_stat=test_base_stats['hp'],
            estimate_hp=True
        )
        assert estimate_ivs_hp == [86]
        estimate_ivs_spcl_def = Pokemon._estimate_stat_ivs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_spcl_def'],
            base_stat=test_base_stats['spcl_def'],
            estimate_hp=False
        )
        assert estimate_ivs_spcl_def == [test_ivs['spcl_def']]

        estimate_phys_def = Pokemon._estimate_stat_ivs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=0.9,
            pokemon_stat=test_pokemon_stats['pokemon_stat_phys_def'],
            base_stat=test_base_stats['phys_def'],
            estimate_hp=False
        )
        assert estimate_phys_def == [5, 6]

    def test_estimate_stat_evs(self, test_pokemon_stats, test_base_stats, test_evs, test_ivs):
        estimate_evs_hp = Pokemon._estimate_stat_evs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_hp'],
            base_stat=test_base_stats['hp'],
            ivs_int=test_ivs['hp'],
            estimate_hp=True
        )
        assert estimate_evs_hp == 252
        estimate_evs_spcl_def = Pokemon._estimate_stat_evs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_spcl_def'],
            base_stat=test_base_stats['spcl_def'],
            ivs_int=test_ivs['spcl_def'], 
            estimate_hp=False
        )
        assert estimate_evs_spcl_def == test_evs['spcl_def']
