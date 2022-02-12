# """Test MainController"""
# import os
# from unittest import mock
# from pokemon_stats_judge.controller.main_controller import MainController


# class TestPokemonController:
#     """ポケモンUseCaseのテスト用クラス
#     """
#     def test_main_controller(self, test_pokemon_stats, test_base_stats):
#         """環境変数をMock化して、努力値と個体値のジャッジ済みの値が返るか確認する。
#         """
#         with mock.patch.dict(os.environ, {'pokemon_name': test_pokemon_stats['pokemon_name']}), \
#             mock.patch.dict(os.environ, {'pokemon_level': str(test_pokemon_stats['pokemon_level'])}), \
#             mock.patch.dict(os.environ, {'pokemon_nature': test_pokemon_stats['pokemon_nature']}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_hp': str(test_pokemon_stats['pokemon_stat_hp'])}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_phys_atk': str(test_pokemon_stats['pokemon_stat_phys_atk'])}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_phys_def': str(test_pokemon_stats['pokemon_stat_phys_def'])}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_spcl_atk': str(test_pokemon_stats['pokemon_stat_spcl_atk'])}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_spcl_def': str(test_pokemon_stats['pokemon_stat_spcl_def'])}), \
#             mock.patch.dict(os.environ, {'pokemon_stat_speed': str(test_pokemon_stats['pokemon_stat_speed'])}):
#             main_controller = MainController()
#             judged_pokemon = main_controller.stats_judge_controller()
#             assert judged_pokemon['pokemon_base_stats']['hp'] == test_base_stats['hp']
#             assert judged_pokemon['pokemon_ivs']['hp'] == [31]
#             assert judged_pokemon['pokemon_evs']['hp'] == 220
