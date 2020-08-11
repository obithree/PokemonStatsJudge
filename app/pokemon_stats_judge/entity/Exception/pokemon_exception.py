


class PokemonException(Exception):
    """PokemonEntityの例外のベースクラス"""
    pass

class InvalidEffortValueException(PokemonException):
    """努力値クラスで送出される例外:一つの努力値が取れない値になっている際のエラー
    属性:
        stat: 能力値のKey名。hp,phys_atkなど。
    """
    def __init__(self, stat, effort_value):
        self.stat = stat
        self.effort_value = effort_value
        pass

    def __str___(self):
        return f'努力値の値が不正です。 {self.stat}: {self.effort_value}'

class InvalidEffortValuesException(PokemonException):
    """努力値クラスで送出される例外: 努力値の合計値が取れない値になっている際のエラー
    """
    def __init__(self, sum_effort_values):
        self.sum_effort_values = sum_effort_values
        pass

    def __str___(self):
        return f'努力値の合計値が不正です。 SUM: {self.sum_effort_values}'

class InvalidIndividualValueException(PokemonException):
    """個体値クラスで送出される例外: 一つの個体値が取れない値になっている際のエラー
    """
    def __init__(self, stat, individual_value):
        self.stat = stat
        self.individual_value = individual_value
        pass

    def __str___(self):
        return f'個体値の値が不正です。 {self.stat}: {self.individual_value}'
