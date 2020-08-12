"""Test PokemonEntity"""
import pytest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException


class TestPokemon:
    """ポケモンエンティティのテスト用クラス
    """

    def test_create_pokemon(self, test_pokemon_stats):
        """種族値個体値努力値を入れずに作成できるかのテスト
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
            test_pokemon_stats['pokemon_stat_speed']
        )
        assert test_pokemon.pokemon_name == test_pokemon_stats['pokemon_name']

    def test_get_dict(self, test_pokemon_stats):
        """get_dictメソッドでdict型を返すかテストする。
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
            test_pokemon_stats['pokemon_stat_speed']
        )
        test_pokemon_dict = test_pokemon.get_dict()
        assert isinstance(test_pokemon_dict, dict)

    def test_is_valid(self, test_pokemon_stats, test_base_stats):
        """個体値、努力値の場所に種族値を入れて"InvalidArgumentTypeException"を返すか確認する。
        """
        pokemon_base_stats = PokemonBaseStats(
            test_base_stats['hp'],
            test_base_stats['phys_atk'],
            test_base_stats['phys_def'],
            test_base_stats['spcl_atk'],
            test_base_stats['spcl_def'],
            test_base_stats['speed']
        )
        with pytest.raises(InvalidArgumentTypeException):
            Pokemon(
                test_pokemon_stats['pokemon_name'],
                test_pokemon_stats['pokemon_level'],
                test_pokemon_stats['pokemon_nature'],
                test_pokemon_stats['pokemon_stat_hp'],
                test_pokemon_stats['pokemon_stat_phys_atk'],
                test_pokemon_stats['pokemon_stat_phys_def'],
                test_pokemon_stats['pokemon_stat_spcl_atk'],
                test_pokemon_stats['pokemon_stat_spcl_def'],
                test_pokemon_stats['pokemon_stat_speed'],
                pokemon_base_stats,
                pokemon_base_stats,
                pokemon_base_stats
            )

    def test_get_pokemon_by_replaced_base_stats(self, test_pokemon_stats, test_base_stats):
        """get_pokemon_by_replaced_base_statsで種族値を置き換えられるか確認する。
        """
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
            test_pokemon_stats['pokemon_stat_speed']
        )
        test_pokemon = test_pokemon.get_pokemon_by_replaced_base_stats(pokemon_base_stats)
        assert test_pokemon.pokemon_base_stats.hp == test_base_stats['hp']

    def test_get_pokemon_by_estimated_ivs_and_evs(self, test_pokemon_stats, test_base_stats):
        """get_pokemon_by_estimated_ivs_and_evsによって個体値と努力値を推測できているか確認する。
        """
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
            test_pokemon_stats['pokemon_stat_speed']
        )
        test_pokemon = test_pokemon.get_pokemon_by_replaced_base_stats(pokemon_base_stats)
        test_pokemon = test_pokemon.get_pokemon_by_estimated_ivs_and_evs()
        assert test_pokemon.pokemon_ivs.hp == [31]
        assert test_pokemon.pokemon_ivs.phys_def == [5, 6]
        assert test_pokemon.pokemon_evs.hp == 220
        assert test_pokemon.pokemon_evs.phys_def == 0
        assert test_pokemon.pokemon_evs.speed == 228

    def test_get_nature_change_dict(self):
        """get_nature_change_dictによって性格による能力変化のリストを取得できるか確認する。
        """
        nature_change_dict = Pokemon._get_nature_change_dict('ひかえめ')
        assert nature_change_dict['spcl_atk'] == 1.1

    def test_estimate_stat_ivs(self, test_pokemon_stats, test_base_stats, test_ivs):
        """_estimate_stat_ivsによっていくつかの能力値の個体値を推測できるか確認する。
        """
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
        assert estimate_ivs_spcl_def == test_ivs['spcl_def']

        estimate_phys_def = Pokemon._estimate_stat_ivs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=0.9,
            pokemon_stat=test_pokemon_stats['pokemon_stat_phys_def'],
            base_stat=test_base_stats['phys_def'],
            estimate_hp=False
        )
        assert estimate_phys_def == [5, 6]

    def test_estimate_stat_evs(self, test_pokemon_stats, test_base_stats, test_evs, test_ivs):
        """_estimate_stat_evsによっていくつかの能力値の努力値を推測できるか確認する。
        """
        estimate_evs_hp = Pokemon._estimate_stat_evs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_hp'],
            base_stat=test_base_stats['hp'],
            ivs_int=test_ivs['hp'][0],
            estimate_hp=True
        )
        assert estimate_evs_hp == 252
        estimate_evs_spcl_def = Pokemon._estimate_stat_evs(
            level=test_pokemon_stats['pokemon_level'],
            nature_change=1.0,
            pokemon_stat=test_pokemon_stats['pokemon_stat_spcl_def'],
            base_stat=test_base_stats['spcl_def'],
            ivs_int=test_ivs['spcl_def'][0],
            estimate_hp=False
        )
        assert estimate_evs_spcl_def == test_evs['spcl_def']
