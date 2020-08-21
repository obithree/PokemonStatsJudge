"""Test EffortValues"""
import pytest
from pokemon_stats_judge.entity.pokemon import PokemonEffortValues
from pokemon_stats_judge.entity.error import InvalidArgumentTypeError
from pokemon_stats_judge.entity.error import InvalidEffortValueError
from pokemon_stats_judge.entity.error import InvalidEffortValuesError


class TestPokemonEffortValues:
    """努力値のテスト用クラス
    """
    def test_create_evs(self, test_evs):
        """正しい値を入れて作成できるか確認する。
        """
        evs = PokemonEffortValues(
            hp=test_evs['hp'],
            phys_atk=test_evs['phys_atk'],
            phys_def=test_evs['phys_def'],
            spcl_atk=test_evs['spcl_atk'],
            spcl_def=test_evs['spcl_def'],
            speed=test_evs['speed']
        )
        assert evs.hp == 252

    def test_get_dict(self, test_evs):
        """get_dictメソッドでdict型を返すかテストする。
        """
        evs = PokemonEffortValues(
            hp=test_evs['hp'],
            phys_atk=test_evs['phys_atk'],
            phys_def=test_evs['phys_def'],
            spcl_atk=test_evs['spcl_atk'],
            spcl_def=test_evs['spcl_def'],
            speed=test_evs['speed']
        )
        evs_dict = evs.get_dict()
        assert isinstance(evs_dict, dict)

    def test_is_valid(self):
        """素早さに入るはずのないlist型を渡して"InvalidArgumentTypeError"が出るか確認する。
        """
        with pytest.raises(InvalidArgumentTypeError):
            PokemonEffortValues(
                hp=252,
                phys_atk=252,
                phys_def=252,
                spcl_atk=252,
                spcl_def=252,
                speed=[252]
            )

    def test_schema_evs_value(self):
        """努力値の最大値255を超えた値を入れるとエラーが出るか確認する。
        """
        with pytest.raises(InvalidEffortValueError):
            PokemonEffortValues(
                hp=300,
                phys_atk=0,
                phys_def=0,
                spcl_atk=0,
                spcl_def=0,
                speed=0
            )
    def test_schema_evs_values(self):
        """努力値の合計が510を超えていないか確認する。
        """
        with pytest.raises(InvalidEffortValuesError):
            PokemonEffortValues(
                hp=252,
                phys_atk=252,
                phys_def=252,
                spcl_atk=252,
                spcl_def=252,
                speed=252
            )
