import sys
import os
from pathlib import Path
from importlib import import_module
from ast import parse,dump
from inspect import getsource
import time

def main():
    args: list[str] = sys.argv[1:]
    compiler_dir: str = os.path.dirname(__file__)
    sys.path.append(str(Path.cwd()))
    sys.path.append(compiler_dir)
    
    commands:set[str] = {'run','build'}
    
    if args[0] not in commands:
        raise Exception('Invalid command!')
    
    if '.py' in args[1]:
        file_name: str = os.path.splitext(args[1])[0]
    else:
        file_name = args[1]
    module = import_module(file_name)
    
    # check if file has a compiler
    if "__COMPILER__" not in dir(module):
        raise Exception("No Compiler '__COMPILER__' detected in file")
    
    sys.path.append(f"{compiler_dir}//{module.__COMPILER__.lower()}")
    
    # compiler 
    compiler = import_module(f'{module.__COMPILER__.lower()}.compiler').PyPoxCompiler()
    
    #print(dump(parse(getsource(module))))
    
    source_codes:list[str] = compiler.compile(parse(getsource(module)))
    
    #print(source_codes)
    if args[0] == 'run':
        os.system(f'node -e "{" ".join(source_codes)}"')
    if args[0] == 'build':
        with open('test.js','x+') as file:
            file.write(f'{" ".join(source_codes)}'.replace('test_class()','new test_class()'))
    

if __name__ == "__main__":
    main()