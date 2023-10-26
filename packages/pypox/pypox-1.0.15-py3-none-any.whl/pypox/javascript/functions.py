from ast import (
    FunctionDef,
    Lambda,
    arguments,
    arg,
    Return,
)

from base import PyPoxBASE

class PyPoxFunctions(PyPoxBASE):
    
    def FUNCTIONDEF(self,node:FunctionDef):
        func_name = self.compile(node.name) #type: ignore
        func_args = self.compile(node.args.args) #type: ignore
        func_body = self.compile(node.body)
        func_return = self.compile(node.returns) #type: ignore
        return f"const {func_name} = ( {','.join(func_args)} ) => {{{''.join(func_body)}}};"
    
    def ARGUMENTS(self,node:arguments):
        return ""
    
    def RETURN(self,node:Return):
        return f"return {self.compile(node.value).replace(';','')};" #type: ignore
    
    def ARG(self,node:arg):
        return f"{node.arg}"
