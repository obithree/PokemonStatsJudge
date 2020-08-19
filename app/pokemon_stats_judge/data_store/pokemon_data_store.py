"""ポケモン集約のrepository"""
import os
import json
from pokemon_stats_judge.repository.pokemon_repository import PokemonRepository
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon_base_stats import PokemonBaseStats
from .Exception.pokemon_data_store_exception import BaseStatsListJsonError
from .Exception.pokemon_data_store_exception import BaseStatsNotFoundError


class PokemonDataStore(PokemonRepository):
    """ポケモン集約のDataStore
    PokemonRepositoryを継承する。
    """

    def get_base_stats(self, pokemon: Pokemon) -> 'PokemonBaseStats':
        """ポケモンの種族値クラスを返す。
        _get_base_stats_dict_from_jsonから、辞書型の種族値リストを取得する。
        その後、_get_pokemon_base_stats_from_base_stats_dictを実行し、種族値クラスを取得し、それを返す。
        """
        pokemon_name = pokemon.pokemon_name
        pokemon_form = 'normal_form'
        pokemons_base_stats_dict = self._get_base_stats_dict_from_json()
        pokemon_base_stats = self._get_pokemon_base_stats_from_base_stats_dict(
            pokemon_name,
            pokemon_form,
            pokemons_base_stats_dict
        )
        return pokemon_base_stats

    @classmethod
    def _get_base_stats_dict_from_json(cls) -> dict:
        """pokemon_base_stats.jsonから、ポケモン種族値リストを取得する。
        このファイルと同じパスに存在する"pokemon_base_stats.json"を読み込む。
        注意："pokemon_base_stats.json"はデプロイ時に正式版に置換予定(権利的な問題で)
        """
        base_stats_json_path = f'{os.path.dirname(__file__)}/pokemon_base_stats.json'
        try:
            with open(base_stats_json_path, encoding="utf-8") as base_stats_json:
                pokemons_base_stats_dict = json.load(base_stats_json)
        except FileNotFoundError as exception_message:
            exception_message = 'ポケモンの種族値リストJsonが存在しません'
            raise BaseStatsListJsonError(exception_message)
        except json.decoder.JSONDecodeError as exception_message:
            exception_message = 'ポケモンの種族値リストのJsonFormatが崩れています。'
            raise BaseStatsListJsonError(exception_message)
        except UnicodeDecodeError as exception_message:
            exception_message = 'ポケモンの種族値リストの文字コードが無効です。UTF-8にしてください'
            raise BaseStatsListJsonError(exception_message)
        return pokemons_base_stats_dict

    @classmethod
    def _get_pokemon_base_stats_from_base_stats_dict(
            cls,
            pokemon_name: str,
            pokemon_form: str,
            pokemons_base_stats_dict: dict) -> dict:
        """種族値リスト(辞書型)から欲しいポケモンの種族値を取得する。
        """
        try:
            pokemon_base_stats_dict = pokemons_base_stats_dict[pokemon_name]
        except KeyError as exception_message:
            exception_message = f'ポケモンの種族値リストに"{exception_message}"というポケモンが見つかりません。'
            raise BaseStatsNotFoundError(exception_message)
        try:
            pokemon_base_stats = PokemonBaseStats(**pokemon_base_stats_dict['base_stats'][pokemon_form])
        except KeyError as exception_message:
            exception_message = f'{pokemon_name}には{pokemon_form}は存在しません。'
            raise BaseStatsNotFoundError(exception_message)
        return pokemon_base_stats
