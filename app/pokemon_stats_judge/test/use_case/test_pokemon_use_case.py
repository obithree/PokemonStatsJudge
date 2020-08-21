"""Test PokemonUsecase"""
import pytest
from unittest import mock
from pokemon_stats_judge.use_case.pokemon_use_case import PokemonUseCase
from pokemon_stats_judge.entity.pokemon_base_stats import PokemonBaseStats
from pokemon_stats_judge.repository.pokemon_repository import PokemonRepository


class TestPokemonUseCase:
    """ポケモンUseCaseのテスト用クラス
    """
    def test_pokemon_status_judge(self, test_pokemon_stats, test_base_stats):
        """ポケモンの実値と名前、性格、レベルを渡す。
        個体値と努力値が推測できているか確認する。
        """
        mock_pokemon_data_store = mock.Mock()
        mock_pokemon_repository = mock_pokemon_data_store(PokemonRepository)
        mock_pokemon_repository.get_base_stats.return_value = PokemonBaseStats(**test_base_stats)
        pokemon_use_case = PokemonUseCase(mock_pokemon_repository)
        judged_pokemon = pokemon_use_case.pokemon_status_judge(request_object=test_pokemon_stats)
        assert judged_pokemon['pokemon_evs']['hp'] == 220
        assert judged_pokemon['pokemon_ivs']['hp'] == [31]

    def test_failed_judge(self, test_pokemon_stats, test_base_stats):
        """誤ったポケモンの実値を渡す。。
        response_objectに失敗したメッセージが入っているか確認する。
        """
        mock_pokemon_data_store = mock.Mock()
        mock_pokemon_repository = mock_pokemon_data_store(PokemonRepository)
        failed_test_pokemon_stats = test_pokemon_stats
        failed_test_pokemon_stats['pokemon_name'] =  'けつばん'
        failed_test_pokemon_stats['pokemon_stat_hp'] = 900
        mock_pokemon_repository.get_base_stats.return_value = PokemonBaseStats(**test_base_stats)
        pokemon_use_case = PokemonUseCase(mock_pokemon_repository)
        judged_pokemon = pokemon_use_case.pokemon_status_judge(request_object=failed_test_pokemon_stats)
        print(judged_pokemon['message'])
        assert judged_pokemon['message'].args == ('hp', 2540)
