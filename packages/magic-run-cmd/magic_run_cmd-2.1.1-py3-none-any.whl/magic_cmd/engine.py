from typing import Protocol, Union

class Engine(Protocol):
    
    def run(cmds:Union[str,list[str]],*args,**kwargs):
        ...
    def write(cmds:Union[str,list[str]],*args,**kwargs):
        ...
