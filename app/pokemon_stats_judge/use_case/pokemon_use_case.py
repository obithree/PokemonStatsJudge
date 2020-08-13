"""ポケモン集約のuse_case"""
# Todo: import方法の統一(全体を一つのModuleとして取れるようにする)
from pokemon_stats_judge.entity.pokemon import Pokemon


class PokemonUseCase:
    """ポケモン集約のUseCase
    """
    def __init__(self) -> None:
        """引数を受け取り初期化する。
        """
        pass

    def pokemon_status_judge(self) -> dict:
        """ポケモンの個体値と努力値を推測し、dictで返す。
        """
        pass
