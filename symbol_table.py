from antlr4.Token import Token
from typing import Any
class SymbolTable():
    def __init__(self):
        self.symbol_table: dict[str, tuple[str, Any]] = {}

    def add_symbol(self, variable: Token, type_: str):
        name = variable.text.strip()
        if name in self.symbol_table:
            print(f"Variable {name} was already declared.")
            return
        self.symbol_table[name] = (type_, 0 if type_ == "int" else 0.0)
        pass

    def get_symbol(self, variable: Token | str):
        name = variable
        if type(variable) != str:
            name = variable.text.strip()
        if name in self.symbol_table:
            return self.symbol_table[name]
        print(f"Variable {name} was not declared.")
        return "error", 0
        pass

    def __setitem__(self, key, value):
        self.add_symbol(key, value)

    def __getitem__(self, item):
        return self.get_symbol(item)