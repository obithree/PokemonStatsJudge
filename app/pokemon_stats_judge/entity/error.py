"""PokemonEntity Error"""
from pokemon_stats_judge.error import PokemonError


class PokemonEntityError(PokemonError):
    """PokemonEntityの例外のベースクラス"""

class InvalidArgumentTypeError(PokemonEntityError):
    """Classのインスタンス化の際に引数の型が異なっている場合のエラー"""
    def __init__(self, argument_name: object, argument_type: type, expected_argument_type: type):
        self.argument_name = argument_name
        self.argument_type = argument_type
        self.expected_argument_type = expected_argument_type


    def __str__(self):
        return f'引数の型が異なります。Argument: {self.argument_name} \nExpected: {self.expected_argument_type}\n Actulal: {self.argument_type}'

class InvalidEffortValueError(PokemonEntityError):
    """努力値クラスで送出される例外:一つの努力値が取れない値になっている際のエラー
    属性:
        stat: 能力値のKey名。hp,phys_atkなど。
    """
    def __init__(self, stat, effort_value):
        self.stat = stat
        self.effort_value = effort_value

    def __str__(self):
        return f'努力値の値が不正です。 {self.stat}: {self.effort_value}'

class InvalidEffortValuesError(PokemonEntityError):
    """努力値クラスで送出される例外: 努力値の合計値が取れない値になっている際のエラー
    """
    def __init__(self, sum_effort_values):
        self.sum_effort_values = sum_effort_values

    def __str__(self):
        return f'努力値の合計値が不正です。 SUM: {self.sum_effort_values}'

class InvalidIndividualValueError(PokemonEntityError):
    """個体値クラスで送出される例外: 一つの個体値が取れない値になっている際のエラー
    """
    def __init__(self, stat, individual_value):
        self.stat = stat
        self.individual_value = individual_value

    def __str__(self):
        return f'個体値の値が不正です。 {self.stat}: {self.individual_value}'
