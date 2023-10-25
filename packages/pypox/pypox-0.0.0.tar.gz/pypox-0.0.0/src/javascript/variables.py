from ast import (
    Name,
    Load,
    Store,
    Del,
    Starred,
)
from base import PyPoxBASE

class PyPoxVariables(PyPoxBASE):
    
    def NAME(self,node:Name):
        
        if isinstance(node.ctx,Load):
            return f"{node.id}"
        
        if isinstance(node.ctx,Store):
            if node.id == node.id.upper():
                return f"const {node.id}"
            else:
                return f"let {node.id}"
        if isinstance(node.ctx,Del):
            return f"delete {node.id}"
    
    def STARRED(self,node:Starred):
        raise Exception("Python Starred not available for convertion")