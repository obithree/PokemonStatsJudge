"""MainController"""
import os
# from app.pokemon_stats_judge.error import PokemonError
from cerberus import Validator
from pokemon_stats_judge.controller.error import InvalidRequestObjectError
from pokemon_stats_judge.controller.request_schema import REQUEST_SCHEMA
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.use_case.pokemon_use_case import PokemonUseCase
from pokemon_stats_judge.data_store.pokemon_data_store import PokemonDataStore

class MainController:
    """PokemonStatsJudgeの汎用Controller。
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

    def stats_judge_controller(self, request_object: dict) -> Pokemon:
        """request_objectを受け取りvalidatorにかけて、それをuse_caseに渡す。
        """
        if not self._validate_request_object(request_object):
            raise InvalidRequestObjectError
        judged_pokemon = self.pokemon_use_case.pokemon_status_judge(request_object)
        return judged_pokemon

    @staticmethod
    def _validate_request_object(request_object: dict) -> None:
        validator = Validator(REQUEST_SCHEMA)
        return validator.validate(request_object)
