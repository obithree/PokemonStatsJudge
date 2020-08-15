"""ポケモン集約のrepository"""
from pokemon_stats_judge.entity.pokemon import Pokemon


class PokemonRepository:
    def __init__(self):
        pass

    def get_base_stats(self, pokemon: Pokemon) -> 'PokemonBaseStats':
        pass
