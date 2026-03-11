#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> str:
        pass
    def format_output(self, result: str)  -> str:
        return f"Output: {result}"
    
