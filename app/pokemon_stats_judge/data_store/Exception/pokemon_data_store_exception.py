"""DataStoreのException一覧"""


class PokemonDataStoreException(Exception):
    """PokemonDataStoreの例外のベースクラス"""

class BaseStatsListJsonError(Exception):
    """ポケモンの種族値リストjson関係のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message

class BaseStatsNotFoundError(Exception):
    """ポケモンの種族値リストにポケモンが見つからない場合のエラー"""
    def __init__(self, error_message):
        self.error_message = error_message

    def __str__(self):
        return self.error_message
