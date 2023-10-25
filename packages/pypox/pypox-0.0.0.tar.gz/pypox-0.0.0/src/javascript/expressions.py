from ast import (
    Attribute,
    BinOp,
    BoolOp,
    Call,
    Compare,
    DictComp,
    Expression,
    Expr,
    GeneratorExp,
    IfExp,
    ListComp,
    NamedExpr,
    SetComp,
    Slice,
    Subscript,
    UnaryOp,
    keyword,
)

from base import PyPoxBASE

class PyPoxExpression(PyPoxBASE):
    
    def EXPRESSION(self,node:Expression):
        return self.compile(node.body) #type: ignore
        
    def EXPR(self,node:Expr):
        return self.compile(node.value) #type: ignore
    
    def UNARYOP(self,node:UnaryOp):
        
        operators:dict[str,str|Exception] = {
            "UADD":Exception("UADD NOT SUPPORTED"),
            "NOT":"!",
            "USUB":"-",
            "INVERT":"~",
        }
        op_name: str | Exception = operators[node.op.__class__.__name__.upper()]
        
        if isinstance(op_name,Exception):
            raise op_name
        
        return f"{op_name}{self.compile(node.operand)}" #type: ignore

    def BINOP(self,node:BinOp):
        
        left = self.compile(node.left)
        right = self.compile(node.right)
        
        operators:dict[str,str|Exception] = {
            "ADD":"+",
            "SUB":"-",
            "MULT":"*",
            "DIV":"/",
            "FLOORDIV":Exception("FLOOR DIV NOT SUPPORTED"),
            "MOD":"%",
            "POW":"**",
            "LSHIFT":"<<",
            "RSHIFT":">>",
            "BITOR":"|",
            "BITXOR":"^",
            "BITAND":"&",
            "MATMUL":Exception("MAT MUL NOT SUPPORTED"),
        }
        
        op_name: str | Exception = operators[node.op.__class__.__name__.upper()]
        
        if isinstance(op_name,Exception):
            raise op_name
        
        return f"{left} {op_name} {right}"
    
    def BOOLOP(self,node:BoolOp) -> None:
        
        operators:dict[str,str] = {
            "AND":"&&",
            "OR":"||"
        }
        
        op_name = operators[node.op.__class__.__name__.upper()]
        
        return f" {op_name} ".join([self.compile(x) for x in node.values]) # type: ignore
        
    def COMPARE(self,node:Compare):
        
        ops_dict = {
            'EQ':'===',
            'NOTEQ':'!==',
            'LT':'<',
            'LTE':'<=',
            'GT':'>',
            'GTE':'>=',
            'IS':'===',
            'ISNOT':'!==',
            'IN':Exception('Not supported'),
            'NOTIN':Exception('Not supported'),
        }
        
        left = self.compile(node.left)
        ops = [ops_dict[x.__class__.__name__.upper()] for x in node.ops]
        comparators = [self.compile(x) for x in node.comparators]
        
        return f"{left} {''.join([f'{o} {c}' for o,c in zip(ops,comparators)])}"  
    
    def CALL(self,node:Call):
        
        if not isinstance(node,Call):
            raise Exception("Invalid ast node must be AST Call")
        
        func_name:str = self.compile(node.func) #type: ignore
        args:list[str] = [self.compile(x) for x in node.args] #type: ignore
        return f"{func_name.replace(';','')}({','.join([x.replace(';','') for x in args])});"
    
    def KEYWORD(self,node:keyword):
        args = self.compile(node.arg) #type: ignore
        value = self.compile(node.value)
    
    def IFEXP(self,node:IfExp):
        
        if not isinstance(node,IfExp):
            raise Exception("Invalid ast node must be AST IfExp")
        
        test:str = self.compile(node.test) #type: ignore
        body:str = self.compile(node.body) #type: ignore
        orelse:str = self.compile(node.orelse) #type: ignore
        
        return "{test} ? {body} : {orelse}".format(
            test=test.replace(';',''),
            body=body.replace(';',''),
            orelse=orelse.replace(';',''),
        ) 
    
    def ATTRIBUTE(self,node:Attribute):
        
        value = getattr(self,node.value.__class__.__name__.upper())(node.value)
        attr = node.attr
        ctx = node.ctx
        
        return f"{value.replace(';','')}.{attr}"
    
    def NAMEDEXPR(self,node:NamedExpr):
        raise Exception("NAMED EXPR NOT SUPPORTED")
    
    def SUBSCRIPT(self,node:Subscript):
        raise Exception("SUBSCRIPT NOT SUPPORTED")
    
    def SLICE(self,node:Slice):
        raise Exception("SLICE NOT SUPPORTED")
    
    def LISTCOMP(self,node:ListComp):
        raise Exception("LISTCOMP NOT SUPPORTED")
    
    def SETCOMP(self,node:SetComp):
        raise Exception("SETCOMP NOT SUPPORTED")
    
    def GENERATOREXP(self,node:GeneratorExp):
        raise Exception("GENERATOREXP NOT SUPPORTED")
    
    def DICTCOMP(self,node:DictComp):
        raise Exception("DICTCOMP NOT SUPPORTED")