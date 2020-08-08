import unittest
from pokemon_stats_judge.entity.pokemon import Pokemon


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
        # pokemon_base_stats = {}
        test_pokemon = Pokemon(
                                pokemon_name,
                                pokemon_stat_level,
                                pokemon_nature,
                                pokemon_stat_hp,
                                pokemon_stat_atk,
                                pokemon_stat_def,
                                pokemon_stat_spcl_atk,
                                pokemon_stat_spcl_def,
                                pokemon_stat_speed
        ) 
        assert test_pokemon.pokemon_name is pokemon_name
