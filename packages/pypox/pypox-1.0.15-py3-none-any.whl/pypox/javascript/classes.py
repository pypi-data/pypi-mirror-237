from ast import (
    ClassDef,
)

from base import PyPoxBASE

class PyPoxClassDef(PyPoxBASE):
    
    def CLASSDEF(self,node:ClassDef):
        class_name = self.compile(node.name) #type: ignore
        class_bases = self.compile(node.bases)
        class_body = self.compile(node.body)
        class_methods = [x.split('=')[0].split(' ')[1] for x in class_body]  #type: ignore
        
        
        class_body = [old.replace(old.split('=')[0],new) for old,new in zip(class_body,class_methods)]  #type: ignore
        
        if class_bases:
            return f"class {class_name} extends {','.join(class_bases)} {{{''.join(class_body)}}};"
        else:
            return f"class {class_name} {{{''.join(class_body)}}};"