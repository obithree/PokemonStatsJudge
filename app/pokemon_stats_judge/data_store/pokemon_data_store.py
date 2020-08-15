"""ポケモン集約のrepository"""
import os
import json
from pokemon_stats_judge.repository.pokemon_repository import PokemonRepository
from pokemon_stats_judge.entity.pokemon import Pokemon
from pokemon_stats_judge.entity.pokemon_base_stats import PokemonBaseStats


class PokemonDataStore(PokemonRepository):
    """ポケモン集約のDataStore
    PokemonRepositoryを継承する。
    """

    @classmethod
    def get_base_stats(cls, pokemon: Pokemon) -> dict:
        """ポケモンの種族値リストのdictを取得する。
        その後、ポケモンの名前で種族値のみを返す。
        このファイルと同じパスに存在する"pokemon_base_stats.json"を読み込む。
        注意："pokemon_base_stats.json"はデプロイ時に正式版に置換予定(権利的な問題で)
        """
        pokemon_name = pokemon.pokemon_name
        base_stats_json_path = f'{os.path.dirname(__file__)}/pokemon_base_stats.json'
        with open(base_stats_json_path, encoding="utf-8") as base_stats_json:
            base_stats_dict = json.load(base_stats_json)
            pokemon_base_stats = PokemonBaseStats(**base_stats_dict[pokemon_name]['base_stats']['normal_form'])
            return pokemon_base_stats
