

from example.components.lexica import MyLexer
from example.components.memory import Memory
from example.components.ast.statement import Expression, Expression_logic, Expression_boolean, Operations
from sly import Parser #Please, ignore IDE warning


class MyParser(Parser):
    debuggable = 'parser.out'
    start = 'statement'

    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens

    precedence = (
        ('left', OR),
        ('left', AND),
    )

    def __init__(self):
        self.memory: Memory = Memory()

    @_('expr')
    def statement(self, p):
        return p.expr


    # E -> E v T
    @_('expr OR term')
    def expr(self, p):
        return p.expr or p.term


    # E -> T
    @_('term')
    def expr(self, p):
        return p.term


    # T -> T ^ F
    @_('term AND factor')
    def term(self, p):
        return p.term and p.factor


    # T -> F
    @_('factor')
    def term(self, p):
        return p.factor


    # F -> t
    @_('T_TRUE')
    def factor(self, p):
        return True


    # F -> f
    @_('F_FALSE')
    def factor(self, p):
        return False



# ---------------- AST VERSION ----------------
class ASTParser(Parser):
    debuggable = 'parser.out'
    start = 'statement'

    tokens = MyLexer.tokens

    precedence = (
        ('left', OR),
        ('left', AND),
    )

    @_('expr')
    def statement(self, p):
        return p.expr   # return root AST -> .run() and .preval()
        

    # Các production giữ nguyên như cũ
    @_('expr OR term')
    def expr(self, p) -> Expression:
        return Expression_logic(Operations.OR, p.expr, p.term)

    @_('term')
    def expr(self, p):
        return p.term

    @_('term AND factor')
    def term(self, p) -> Expression:
        return Expression_logic(Operations.AND, p.term, p.factor)

    @_('factor')
    def term(self, p):
        return p.factor

    @_('T_TRUE')
    def factor(self, p) -> Expression:
        return Expression_boolean(True)

    @_('F_FALSE')
    def factor(self, p) -> Expression:
        return Expression_boolean(False)



if __name__ == "__main__":
    lexer = MyLexer()
    parser = ASTParser()
    text = "t ^ f v t"
    result = parser.parse(lexer.tokenize(text))
    print("Result:", result)