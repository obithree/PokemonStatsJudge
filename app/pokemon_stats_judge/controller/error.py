"""PokemonEntity Error"""
from pokemon_stats_judge.error import PokemonError


class ControllerError(PokemonError):
    """Controllerの例外のベースクラス"""

class InvalidRequestObjectError(ControllerError):
    """RequestObjectがスキーマ通り作られていない際のエラー"""
    def __init__(self): 
        pass

    def __str__(self):
        return f'正しくRequestObjectが作成されていません。'
