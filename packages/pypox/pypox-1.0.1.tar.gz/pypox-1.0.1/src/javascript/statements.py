from ast import (
    Assign,
    AnnAssign,
    AugAssign,
    Raise,
    Assert,
    Delete,
    Pass,
    Import,
    ImportFrom,
    alias,
)
from base import PyPoxBASE

class PyPoxStatements(PyPoxBASE):
    
    def ASSIGN(self,node:Assign):
        
        targets:list[str] = [self.compile(x) for x in node.targets] #type: ignore
        value:str = self.compile(node.value) #type: ignore
        
        return f"{','.join(targets)} = {value.replace(';','')};"
    
    def ANNASSIGN(self,node:AnnAssign):
        raise Exception("ANN-ASSIGN NOT SUPPORTED")
    
    def AUGASSIGN(self,node:AugAssign):
        
        operators:dict[str,str] = {
            "ADD":"+=",
            "SUB":"-=",
            "MULT":"*=",
            "DIV":"/=",
            "MOD":"%=",
        }
        target:str = self.compile(node.target) #type: ignore
        value:str = self.compile(node.value) #type: ignore
        op_name:str = operators[node.op.__class__.__name__.upper()]
        return f"{target.split(' ')[1:][0]} {op_name} {value};"
    
    def RAISE(self,node:Raise):
        return ""
    
    def ASSERT(self,node:Raise):
        raise Exception("ASSERT NOT SUPPORTED")
    
    def DELETE(self,node:Raise):
        raise Exception("DELETE NOT SUPPORTED")
    
    def PASS(self,node:Raise):
        return "/* pass */"
    
    def IMPORT(self,node:Raise):
        return ""
    
    def IMPORTFROM(self,node:Raise):
        return ""