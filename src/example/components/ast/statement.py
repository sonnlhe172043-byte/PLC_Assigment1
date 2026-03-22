from enum import Enum
from abc import ABC, abstractmethod


class Statement:
    def __init__(self, root_node):
        self.root_node = root_node

    def run(self):
        self.root_node.run()
        return self.root_node.value


class Operations(Enum):
    AND = 0 # SỬA LẠI
    OR = 1


class Expression(ABC):
    def __init__(self):
        self.signature = ""
        self.value = None

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def preval(self) -> str:

        pass


class Expression_logic(Expression):
    def __init__(self, operation: Operations, parameter1: Expression, parameter2: Expression):
        super().__init__()
        assert isinstance(operation, Operations)
        self.operation = operation
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.children = [parameter1, parameter2]

    def run(self):
        # evaluate children first
        for child in self.children:
            child.run()

        if self.operation == Operations.AND:
            self.value = self.parameter1.value and self.parameter2.value
        elif self.operation == Operations.OR:
            self.value = self.parameter1.value or self.parameter2.value

        self.signature = f"{self.parameter1.value} {self.operation.name} {self.parameter2.value}"
        print(self)

    def preval(self) -> str:
        #  semantic rule for prefix
        op = "^" if self.operation == Operations.AND else "v"

        # E -> E1 v T   or   T -> T1 ^ F
        # preval := op + " " + left.preval + " " + right.preval
        left_pre = self.parameter1.preval()
        right_pre = self.parameter2.preval()

        return f"{op} {left_pre} {right_pre}"

    def __repr__(self):
        return f"Expression_logic:{self.signature}"


class Expression_boolean(Expression):
    def __init__(self, value: bool):
        super().__init__()
        self.value = value
        self.signature = str(value)

    def run(self):
        print(self)

    def preval(self) -> str:
        # F -> t   hoặc   F -> f
        # preval := t.lexval hoặc f.lexval
        return "t" if self.value else "f"

    def __repr__(self):
        return f"Expression_boolean:{self.value}"