"""Test BaseStats"""
import pytest
from pokemon_stats_judge.entity.pokemon import PokemonBaseStats
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException


class TestPokemonBaseStats:
    """種族値のテスト用クラス
    """
    def test_create_base_stats(self, test_base_stats):
        """正しい値を入れて作成できるか確認する。
        """
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
        """get_dictメソッドでdict型を返すかテストする。
        """
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
        """hpに入るはずのないlist型を渡して"InvalidArgumentTypeException"が出るか確認する。
        """
        with pytest.raises(InvalidArgumentTypeException):
            PokemonBaseStats(
                [100],
                test_base_stats['phys_atk'],
                test_base_stats['phys_def'],
                test_base_stats['spcl_atk'],
                test_base_stats['spcl_def'],
                test_base_stats['speed']
            )
