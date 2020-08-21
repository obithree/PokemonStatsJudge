"""PokemonDataStoreError"""
from pokemon_stats_judge.error import PokemonError


class PokemonDataStoreError(PokemonError):
    """PokemonDataStoreの例外のベースクラス"""

class BaseStatsListJsonError(PokemonDataStoreError):
    """ポケモンの種族値リストjson関係のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

class BaseStatsNotFoundError(PokemonDataStoreError):
    """ポケモンの種族値リストにポケモンが見つからない場合のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
