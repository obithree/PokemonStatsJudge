"""DataStoreのException一覧"""
from pokemon_stats_judge.error import PokemonError


class PokemonDataStoreException(PokemonError):
    """PokemonDataStoreの例外のベースクラス"""

class BaseStatsListJsonError(PokemonDataStoreException):
    """ポケモンの種族値リストjson関係のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

class BaseStatsNotFoundError(PokemonDataStoreException):
    """ポケモンの種族値リストにポケモンが見つからない場合のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
