"""ポケモン集約のuse_case"""
# Todo: import方法の統一(全体を一つのModuleとして取れるようにする)
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.repository.pokemon_repository import PokemonRepository
from pokemon_stats_judge.error import PokemonError
from pokemon_stats_judge.entity.error import InvalidArgumentTypeError
from pokemon_stats_judge.entity.error import InvalidEffortValueError
from pokemon_stats_judge.entity.error import InvalidEffortValuesError
from pokemon_stats_judge.entity.error import InvalidIndividualValueError


class PokemonUseCase:
    """ポケモン集約のUseCase
    """
    def __init__(self, pokemon_repository: PokemonRepository) -> None:
        """引数を受け取り初期化する。
        """
        self.pokemon_repository = pokemon_repository

    def pokemon_status_judge(self, request_object: dict) -> dict:
        """ポケモンの個体値と努力値を推測し、dictで返す。
        """
        try:
            pokemon = Pokemon(**request_object)
            pokemon_base_stats = self.pokemon_repository.get_base_stats(pokemon)
            pokemon_got_base_stats = pokemon.get_pokemon_by_replaced_base_stats(pokemon_base_stats)
        except (InvalidArgumentTypeError, PokemonError) as error_message:
            response_object = {"message": error_message}
            return response_object
        try:
            judged_pokemon = pokemon_got_base_stats.get_pokemon_by_estimated_ivs_and_evs()
        except (InvalidEffortValuesError, InvalidEffortValueError, InvalidIndividualValueError) as error_message:
            response_object = {"message": error_message}
            return response_object
        return judged_pokemon.get_dict()
