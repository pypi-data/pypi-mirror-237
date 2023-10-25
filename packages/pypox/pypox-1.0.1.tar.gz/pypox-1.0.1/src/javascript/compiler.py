from typing import Any
import ast
import copy
from literal import PyPoxLiteral
from variables import PyPoxVariables
from expressions import PyPoxExpression
from statements import PyPoxStatements
from control_flow import PyPoxControlFlow
from functions import PyPoxFunctions
from classes import PyPoxClassDef
class PyPoxCompiler(
    PyPoxLiteral,
    PyPoxVariables,
    PyPoxExpression,
    PyPoxStatements,
    PyPoxControlFlow,
    PyPoxFunctions,
    PyPoxClassDef,
):
    
    # helper functions
        
    def compile(self,ast_node:ast.Module | Any) -> list[str] | str:
        
        if not ast_node:
            return ast_node
        
        if isinstance(ast_node,ast.Module):
            return self.compile(ast_node.body)
        
        if isinstance(ast_node,list):
            body = []
            for node in ast_node:
                body.append(self.compile(node))
            if not all(isinstance(x,str) for x in body):
                return self.compile(body)
            return body    
        
        name = ast_node.__class__.__name__.upper()
        
        if name == 'STR':
            return ast_node
        
        return getattr(self,ast_node.__class__.__name__.upper())(ast_node)
    
if __name__ == "__main__":
    pass