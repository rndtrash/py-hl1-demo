from hl1demo.BaseDemoParser import BaseDemoParser
from hl1demo.macros import BaseMacro


class CS16DemoParser(BaseDemoParser):
    def __init__(self, bs):
        super().__init__(bs, 5, 47, 'cstrike')

    def get_macro_by_id(self, base_macro: BaseMacro) -> BaseMacro:
        # TODO: add CS1.6-specific macros

        return BaseDemoParser.get_macro_by_id(self, base_macro)
