"""Test PokemonUsecase"""
import pytest
from pokemon_stats_judge.use_case.pokemon_use_case import PokemonUseCase


class TestPokemonUseCase:
    """ポケモンUseCaseのテスト用クラス
    """
    def test_pokemon_status_judge(self):
        """ポケモンの実値と名前、性格、レベルを渡す。
        個体値と努力値が推測できているか確認する。
        """
        pokemon_use_case = PokemonUseCase()
        pokemon_use_case.pokemon_status_judge()
        pass
