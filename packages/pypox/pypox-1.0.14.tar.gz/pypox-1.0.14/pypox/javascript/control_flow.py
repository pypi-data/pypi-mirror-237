from ast import (
    ExceptHandler,
    If,
    For,
    Try,
    TryStar,
    While,
    Break,
    Continue,
    withitem,
)

from base import PyPoxBASE

class PyPoxControlFlow(PyPoxBASE):
    
    def IF(self,node:If) -> str:
        
        test: str = self.compile(node.test)  #type: ignore
        body: str = self.compile(node.body)  #type: ignore
        orelse: str = self.compile(node.orelse)  #type: ignore
        
        if orelse:
            if isinstance(node.orelse[0],If):
                return "if ( {test} ) {{ {body} }} else {orelse} ".format(
                    test=test.replace(';',''),
                    body=" ".join(body),
                    orelse=" ".join(orelse)
                )
            else:
                return "if ( {test} ) {{ {body} }} else {{ {orelse} }}".format(
                    test=test.replace(';',''),
                    body=" ".join(body),
                    orelse=" ".join(orelse)
                )
        else:
            return "if ( {test} ) {{ {body} }}".format(
                test=test.replace(';',''),
                body=" ".join(body)
            )
        
    def FOR(self,node:For) -> str:
        
        target = self.compile(node.target)
        iter_ = self.compile(node.iter)  #type: ignore
        body = self.compile(node.body)
        orelse = self.compile(node.orelse)
        
        if orelse:
            return "for ( {target} of {iter} ) {{ {body} }} {orelse} ".format(
                target=target.replace(';',''),  #type: ignore
                iter=iter_.replace(';',''),  #type: ignore
                body=''.join(body),  #type: ignore
                orelse=''.join(orelse)  #type: ignore
            )
        
        return "for ( {target} of {iter} ) {{ {body} }} ".format(
                target=target.replace(';',''),  #type: ignore
                iter=iter_.replace(';',''),  #type: ignore
                body=''.join(body)  #type: ignore
            ) 
        
    def WHILE(self,node:While) -> str:
        
        test:str = self.compile(node.test)  #type: ignore
        body:str = self.compile(node.body)  #type: ignore
        orelse:str = self.compile(node.orelse)  #type: ignore 
        
        if orelse:
            return "while ( {test} ) {{ {body} }} {orelse}".format(
                test=test,
                body=' '.join(body),
                orelse=' '.join(orelse)
            )
        else:
            return "while ( {test} ) {{ {body} }}".format(
                    test=test,
                    body=' '.join(body),
                )
    
    def BREAK(self,node:Break) -> str:
        return "break;"
    
    def CONTINUE(self,node:Continue) -> str:
        return "continue;"
    
    def TRY(self,node:Try):
        try_block = self.compile(node.body)
        handlers = self.compile(node.handlers)
        #orelse = self.compile(node.orelse)
        #final_body = self.compile(node.finalbody)
        
        try_str:str = "try {{{try_block}}}".format(
            try_block=''.join(try_block)  #type: ignore
        ) #type: ignore
        catch_str = " ".join(handlers) #type: ignore
        
        return f"{try_str} {catch_str}"
        
    def TRYSTAR(self,node:TryStar):
        raise Exception('TRYSTAR NOT SUPPORTED')
    
    def EXCEPTHANDLER(self,node:ExceptHandler):
        catch_type: str = self.compile(node.type) #type: ignore
        catch_name: str = self.compile(node.name) #type: ignore
        catch_body: str = self.compile(node.body) #type: ignore
        
        return f"catch ({catch_type}) {{{''.join(catch_body)}}}"
    
    def WITH(self,node:Try):
        raise Exception('WITH NOT SUPPORTED')
    
    def WITHITEM(self,node:withitem):
        raise Exception('WITH ITEM NOT SUPPORTED')