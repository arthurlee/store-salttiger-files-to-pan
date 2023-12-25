from collections.abc import Iterable
from typing import Any


class Record(dict):
    def __setattr__(self, name, value):
        self[name] = value
            
    def __getattr__(self, name):
        return self[name]
    
    def __delattr__(self, name):
        del self[name]
    
    def __dir__(self) -> Iterable[str]:
        return list(self) + list(type(self))
