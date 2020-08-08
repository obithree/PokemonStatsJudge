import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats

class TestPokemon(unittest.TestCase):
    """test class of pokemon entity
    """

    def test_create_pokemon(self):
        """test pokemon entity create
        """
        pokemon_stat_level = 100
        pokemon_name = 'ヒノヤコマ'
        pokemon_stat_level = 100
        pokemon_nature = 'せっかち'
        pokemon_stat_hp = 320
        pokemon_stat_atk = 170
        pokemon_stat_def = 109
        pokemon_stat_spcl_atk = 287
        pokemon_stat_spcl_def = 138
        pokemon_stat_speed = 113
        # Todo:ポケモンの種族値取得も含めてテスト
        pokemon_base_hp = 62
        pokemon_base_atk = 73
        pokemon_base_def = 55
        pokemon_base_spcl_atk = 56
        pokemon_base_spcl_def = 52
        pokemon_base_speed = 84
        pokemon_base_stats = PokemonBaseStats(
            pokemon_name,
            pokemon_base_hp,
            pokemon_base_atk,
            pokemon_base_def,
            pokemon_base_spcl_atk,
            pokemon_base_spcl_def,
            pokemon_base_speed
        )


        test_pokemon = Pokemon(
                                pokemon_name,
                                pokemon_stat_level,
                                pokemon_nature,
                                pokemon_stat_hp,
                                pokemon_stat_atk,
                                pokemon_stat_def,
                                pokemon_stat_spcl_atk,
                                pokemon_stat_spcl_def,
                                pokemon_stat_speed,
                                pokemon_base_stats
        ) 
        assert test_pokemon.pokemon_name is pokemon_name
        assert test_pokemon.pokemon_base_stats.pokemon_base_hp is pokemon_base_hp
