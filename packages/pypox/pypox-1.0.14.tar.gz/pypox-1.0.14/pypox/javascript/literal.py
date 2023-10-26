from ast import (
    Constant,
    FormattedValue,
    JoinedStr,
    List,
    Load,
    Tuple,
    Set,
    Dict,
    parse,
    dump
)
from base import PyPoxBASE

class PyPoxLiteral(PyPoxBASE):
    
    def CONSTANT(self,node:Constant) -> str:
        
        if isinstance(node.value,str):
            return f"'{node.value}'"
        else:
            return f"{node.value}"

    def FORMATTEDVALUE(self,node:FormattedValue) -> str:
        return ""

    def JOINEDSTR(self,node:JoinedStr):
        
        for val in node.values:
            pass

    def LIST(self,node: List) -> str:
        
        if isinstance(node.ctx,Load):
            return f"[{','.join([self.compile(x) for x in node.elts])}]" #type: ignore
        
        return ""

    def TUPLE(self,node: Tuple) -> str:
        
        if isinstance(node.ctx,Load):
            return f"[{','.join([self.compile(x) for x in node.elts])}]" #type: ignore
        
        return ""
    
    def SET(self,node: Set) -> str:
        
        return f"new Set([{','.join([self.compile(x) for x in node.elts])}])" #type: ignore

    def DICT(self,node: Dict) -> str:
        
        pairs:list[str] = []
        
        for key,val in zip(node.keys,node.values):
            pairs.append(f"{self.compile(key)}:{self.compile(val)}") #type: ignore

        return "{" + ",".join(pairs) + "}"