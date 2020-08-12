"""Test IndividualValues"""
import pytest
from pokemon_stats_judge.entity.pokemon import PokemonIndividualValues
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidArgumentTypeException
from pokemon_stats_judge.entity.Exception.pokemon_exception import InvalidIndividualValueException


class TestPokemonIndividualValues:
    """個体値のテスト用クラス
    """
    def test_create_ivs(self, test_ivs):
        """正しい値を入れて作成できるか確認する。
        """
        ivs = PokemonIndividualValues(
            hp=test_ivs['hp'],
            phys_atk=test_ivs['phys_atk'],
            phys_def=test_ivs['phys_def'],
            spcl_atk=test_ivs['spcl_atk'],
            spcl_def=test_ivs['spcl_def'],
            speed=test_ivs['speed']
        )
        assert ivs.hp[0] == 23

    def test_get_dict(self, test_ivs):
        """get_dictメソッドでdict型を返すかテストする。
        """
        ivs = PokemonIndividualValues(
            hp=test_ivs['hp'],
            phys_atk=test_ivs['phys_atk'],
            phys_def=test_ivs['phys_def'],
            spcl_atk=test_ivs['spcl_atk'],
            spcl_def=test_ivs['spcl_def'],
            speed=test_ivs['speed']
        )
        ivs_dict = ivs.get_dict()
        assert isinstance(ivs_dict, dict)

    def test_is_valid(self):
        """入るはずのないlist型を渡して"InvalidArgumentTypeException"が出るか確認する。
        """
        with pytest.raises(InvalidArgumentTypeException):
            PokemonIndividualValues(
                hp=[7, 8],
                phys_atk=[7, 8],
                phys_def=[7, 8],
                spcl_atk=[7, 8],
                spcl_def=[7, 8],
                speed=31
            )

    def test_schema_ivs_value(self):
        """個体値の最大の31を超えた数字を入れた場合、"InvalidIndividualValueException"が出るか確認する。
        """
        with pytest.raises(InvalidIndividualValueException):
            PokemonIndividualValues(
                hp=[7, 8],
                phys_atk=[7, 8],
                phys_def=[7, 8],
                spcl_atk=[7, 8],
                spcl_def=[7, 8],
                speed=[39]
            )
