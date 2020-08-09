import pytest


@pytest.fixture(autouse=True, scope='class')
def test_base_stats():
    hinoyakoma_base_stats = {
        'pokemon_name': 'ヒノヤコマ',
        'base_hp': 62,
        'base_atk': 73,
        'base_def': 55,
        'base_spcl_atk': 56,
        'base_spcl_def': 52,
        'base_speed': 84
    }
    print(hinoyakoma_base_stats)
    return hinoyakoma_base_stats

@pytest.fixture(autouse=True, scope='class')
def test_pokemon_stats():
    hinoyakoma_stats = {
        'pokemon_name': 'ヒノヤコマ',
        'pokemon_stat_level': 100,
        'pokemon_nature': 'せっかち',
        'pokemon_stat_hp': 320,
        'pokemon_stat_atk': 170,
        'pokemon_stat_def': 108,
        'pokemon_stat_spcl_atk': 138,
        'pokemon_stat_spcl_def': 113,
        'pokemon_stat_speed': 287
    }
    return hinoyakoma_stats

@pytest.fixture(autouse=True, scope='class')
def test_ivs():
    hinoyakoma_ivs = {
        "ivs_hp": 23,
        "ivs_atk": 19,
        "ivs_def": 6,
        "ivs_spcl_atk": 21,
        "ivs_spcl_def": 4,
        "ivs_speed": 25
    }
    return hinoyakoma_ivs

@pytest.fixture(autouse=True, scope='class')
def test_evs():
    hinoyakoma_evs = {
        "evs_hp": 252,
        "evs_atk": 0,
        "evs_def": 0,
        "evs_spcl_atk": 0,
        "evs_spcl_def": 0,
        "evs_speed": 252
    }
    return hinoyakoma_evs
