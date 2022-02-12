"""Test MainController"""
import os
import pytest
from unittest import mock
from pokemon_stats_judge.controller.error import InvalidRequestObjectError
from pokemon_stats_judge.controller.main_controller import MainController


class TestPokemonController:
    """ポケモンUseCaseのテスト用クラス
    """
    @pytest.mark.parametrize("test_pokemon_request, success, expected_ivs, expected_evs", [
        (
            {
                'pokemon_name': 'ヒノヤコマ',
                'pokemon_level': 100,
                'pokemon_nature': 'せっかち',
                'pokemon_stat_hp': 320,
                'pokemon_stat_phys_atk': 170,
                'pokemon_stat_phys_def': 108,
                'pokemon_stat_spcl_atk': 138,
                'pokemon_stat_spcl_def': 113,
                'pokemon_stat_speed': 287
            },
            True,
            {
                "hp": [31],
                "phys_atk": [19],
                "phys_def": [5, 6],
                "spcl_atk": [21],
                "spcl_def": [4],
                "speed": [31]
            },
            {
                "hp": 220,
                "phys_atk": 0,
                "phys_def": 0,
                "spcl_atk": 0,
                "spcl_def": 0,
                "speed": 228
            }
        ),
        # NOTE: スキーマエラー
        (
            {
                'pokemon_name': 'ヒノヤコマ',
                # NOTE: レベルをstringにする。
                'pokemon_level': '100',
                'pokemon_nature': 'せっかち',
                'pokemon_stat_hp': 320,
                'pokemon_stat_phys_atk': 170,
                'pokemon_stat_phys_def': 108,
                'pokemon_stat_spcl_atk': 138,
                'pokemon_stat_spcl_def': 113,
                'pokemon_stat_speed': 287
            },
            False,
            {
                "hp": [31],
                "phys_atk": [19],
                "phys_def": [5, 6],
                "spcl_atk": [21],
                "spcl_def": [4],
                "speed": [31]
            },
            {
                "hp": 220,
                "phys_atk": 0,
                "phys_def": 0,
                "spcl_atk": 0,
                "spcl_def": 0,
                "speed": 228
            }
        )
    ])
    def test_main_controller(
            self, test_base_stats,success, 
            test_pokemon_request, expected_ivs, expected_evs
        ):
        """環境変数をMock化して、努力値と個体値のジャッジ済みの値が返るか確認する。
        """
        main_controller = MainController()
        if success:
            judged_pokemon = main_controller.stats_judge_controller(test_pokemon_request)
            assert judged_pokemon['pokemon_base_stats'] == test_base_stats
            assert judged_pokemon['pokemon_ivs'] == expected_ivs
            assert judged_pokemon['pokemon_evs'] == expected_evs
        else:
            with pytest.raises(InvalidRequestObjectError):
                judged_pokemon = main_controller.stats_judge_controller(test_pokemon_request)
