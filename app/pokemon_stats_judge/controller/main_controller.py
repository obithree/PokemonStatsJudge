"""MainController"""
import os
from pokemon_stats_judge.use_case.pokemon_use_case import PokemonUseCase
from pokemon_stats_judge.data_store.pokemon_data_store import PokemonDataStore

class MainController:
    """AWS Lambda用のController
    環境変数で受け取ったポケモンの名前やレベル、性格、ステータスをreqest_objectにしてuse_caseに渡す。
    """
    def __init__(self):
        """初期化時の処理
            data_storeをインスタンス化し、それをuse_caseに渡す。
            ※use_caseはrepositoryを受け取るが、data_storeはrepositoryはそれを継承している。
        """
        self.pokemon_data_store = PokemonDataStore()
        self.pokemon_use_case = PokemonUseCase(
            pokemon_repository=self.pokemon_data_store
        )

    def stats_judge_controller(self):
        """request_objectを"_get_request_object"から作成し、それをuse_caseに渡す。
        """
        request_object = self._get_request_object()
        judged_pokemon = self.pokemon_use_case.pokemon_status_judge(request_object)
        return judged_pokemon

    def _get_request_object(self):
        """request_objectを環境変数から作成する。
        """
        request_object = {
            'pokemon_name': os.environ['pokemon_name'],
            'pokemon_level': int(os.environ['pokemon_level']),
            'pokemon_nature': os.environ['pokemon_nature'],
            'pokemon_stat_hp': int(os.environ['pokemon_stat_hp']),
            'pokemon_stat_phys_atk': int(os.environ['pokemon_stat_phys_atk']),
            'pokemon_stat_phys_def': int(os.environ['pokemon_stat_phys_def']),
            'pokemon_stat_spcl_atk': int(os.environ['pokemon_stat_spcl_atk']),
            'pokemon_stat_spcl_def': int(os.environ['pokemon_stat_spcl_def']),
            'pokemon_stat_speed': int(os.environ['pokemon_stat_speed'])
        }
        return request_object
