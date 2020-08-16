"""Test LambdaController"""
import pytest
import os
from unittest import mock
from pokemon_stats_judge.use_case.pokemon_use_case import PokemonUseCase
from pokemon_stats_judge.controller.lambda_controller import LambdaController


class TestPokemonController:
    """ポケモンUseCaseのテスト用クラス
    """
    def test_lambda_controller(self, test_pokemon_stats, test_base_stats):
        """環境変数をMock化して、努力値と個体値のジャッジ済みの値が返るか確認する。
        """
        with mock.patch.dict(os.environ, {'pokemon_name': test_pokemon_stats['pokemon_name']}), \
            mock.patch.dict(os.environ, {'pokemon_level': str(test_pokemon_stats['pokemon_level'])}), \
            mock.patch.dict(os.environ, {'pokemon_nature': test_pokemon_stats['pokemon_nature']}), \
            mock.patch.dict(os.environ, {'pokemon_stat_hp': str(test_pokemon_stats['pokemon_stat_hp'])}), \
            mock.patch.dict(os.environ, {'pokemon_stat_phys_atk': str(test_pokemon_stats['pokemon_stat_phys_atk'])}), \
            mock.patch.dict(os.environ, {'pokemon_stat_phys_def': str(test_pokemon_stats['pokemon_stat_phys_def'])}), \
            mock.patch.dict(os.environ, {'pokemon_stat_spcl_atk': str(test_pokemon_stats['pokemon_stat_spcl_atk'])}), \
            mock.patch.dict(os.environ, {'pokemon_stat_spcl_def': str(test_pokemon_stats['pokemon_stat_spcl_def'])}), \
            mock.patch.dict(os.environ, {'pokemon_stat_speed': str(test_pokemon_stats['pokemon_stat_speed'])}):
            
            lambda_controller = LambdaController()
            judged_pokemon = lambda_controller.stats_judge_controller()
            assert judged_pokemon['pokemon_base_stats']['hp'] == 62
            assert judged_pokemon['pokemon_ivs']['hp'] == [31]
            assert judged_pokemon['pokemon_evs']['hp'] == 220
