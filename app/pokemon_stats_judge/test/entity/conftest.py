import pytest


@pytest.fixture(autouse=True, scope='class')
def test_base_stats():
    hinoyakoma_base_stats = {
        'hp': 62,
        'phys_atk': 73,
        'phys_def': 55,
        'spcl_atk': 56,
        'spcl_def': 52,
        'speed': 84
    }
    return hinoyakoma_base_stats

@pytest.fixture(autouse=True, scope='class')
def test_pokemon_stats():
    hinoyakoma_stats = {
        'pokemon_name': 'ヒノヤコマ',
        'pokemon_level': 100,
        'pokemon_nature': 'せっかち',
        'pokemon_stat_hp': 320,
        'pokemon_stat_phys_atk': 170,
        'pokemon_stat_phys_def': 108,
        'pokemon_stat_spcl_atk': 138,
        'pokemon_stat_spcl_def': 113,
        'pokemon_stat_speed': 287
    }
    return hinoyakoma_stats

@pytest.fixture(autouse=True, scope='class')
def test_ivs():
    hinoyakoma_ivs = {
        "hp": [23],
        "phys_atk": [19],
        "phys_def": [5, 6],
        "spcl_atk": [21],
        "spcl_def": [4],
        "speed": [25]
    }
    return hinoyakoma_ivs

@pytest.fixture(autouse=True, scope='class')
def test_evs():
    hinoyakoma_evs = {
        "hp": 252,
        "phys_atk": 0,
        "phys_def": 0,
        "spcl_atk": 0,
        "spcl_def": 0,
        "speed": 252
    }
    return hinoyakoma_evs
