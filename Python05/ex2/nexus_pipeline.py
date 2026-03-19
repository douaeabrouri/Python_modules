#!/usr/bin/env python3

# pipeline → stages → process data step by step

# data
#  ↓
# InputStage
#  ↓
# TransformStage
#  ↓
# OutputStage

from abc import ABC, abstractmethod
from typing import Protocol, Any

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...

class ProcessingPipeline(ABC):

    def __init__(self, pipline_id: str) -> None:
       self.pipline_id = pipline_id
       self.stages: list[ProcessingStage] = []
    
    def add_stages(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)
    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

class InputStage():
    pass
class TransformStage():
    pass
class OutputStage():
    pass
