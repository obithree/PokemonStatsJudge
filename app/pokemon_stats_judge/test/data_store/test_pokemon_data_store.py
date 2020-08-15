"""Test Pokemon DataStore"""
import pytest
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.repository.pokemon_repository import PokemonRepository
from pokemon_stats_judge.data_store.pokemon_data_store import PokemonDataStore


class TestPokemonDataStore:
    """ポケモン集約のDataStore用テスト
    """
    def test_get_base_stats(self, test_pokemon_stats, test_base_stats) -> 'PokemonBaseStats':
        """ポケモンEntityを渡して、正しい種族値が帰ってくるか確認する。
        """
        #pokemon_repository = PokemonRepository()
        test_pokemon = Pokemon(**test_pokemon_stats)
        pokemon_data_store = PokemonDataStore()
        test_pokemon_base_stats = pokemon_data_store.get_base_stats(test_pokemon)
        assert test_pokemon_base_stats.get_dict() == test_base_stats['hp']
