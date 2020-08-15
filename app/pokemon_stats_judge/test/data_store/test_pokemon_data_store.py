"""Test Pokemon DataStore"""
from pokemon_stats_judge.entity.pokemon import Pokemon
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
        assert test_pokemon_base_stats.get_dict()['hp'] == test_base_stats['hp']
        assert test_pokemon_base_stats.get_dict()['phys_atk'] == test_base_stats['phys_atk']
        assert test_pokemon_base_stats.get_dict()['phys_def'] == test_base_stats['phys_def']
        assert test_pokemon_base_stats.get_dict()['spcl_atk'] == test_base_stats['spcl_atk']
        assert test_pokemon_base_stats.get_dict()['spcl_def'] == test_base_stats['spcl_def']
        assert test_pokemon_base_stats.get_dict()['speed'] == test_base_stats['speed']
