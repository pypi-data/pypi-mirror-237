from __future__ import annotations
from typing import (
                    Union, 
                    Callable, 
)
from pathlib import Path
from magic_cmd.engine import Engine 
from magic_cmd.run_cmd import Shell


class Script():
    
    '''
        Allows you write bash scripts in python code.
        script = Scripts()
        script.cmds = """
                        ls
                        echo "an"
                       """
        script()
    '''
    
    def __init__(self,
                 cmds:str='',
                 name:str= 'script',
                 engine:Engine=Shell,
                ):
        self.cmds:str = cmds
        self.engine:Engine = engine
        self.name:str = name

    def __add__(self,cmd: Union[Script,str])->str:
        match(cmd):
            case str():cmds:str =  '\n'.join([self.cmds,cmd])
            case Script() if self.engine!=cmd.engine:
                raise Exception(f'{self.engine.__name__} do not match {cmd.engine.__name__}')
            case Script():cmds:str = '\n'.join([self.cmds,cmd.cmd])
        return Script(cmds)
    
    def __iadd__(self,cmd: Union[Script,str])->Script:
        self = self + cmd
        return self
    
    def __repr__(self) -> str:
        return self.cmds
    
    def __str__(self) -> str:
        return self.cmds
     
    def __call__(self,
                 lazy:bool=False,
                 name:str='lazy',
                 split:bool='False',
                 *args,**kwargs) -> Union[Path,list[str]]:
        if lazy:
            return self.engine.write(self.cmds,name=name)
        return self.engine.run(self.cmds,split=split)
        

    def append(self,cmd:Union[Script,str])->None:
        self.cmds += cmd
        