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
import json

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
    def process(self, data: Any) -> Any:
        return f"Input: {data}"
class TransformStage():
    def process(self, data: Any) -> Any:
        return f"Transfor: {str(data).upper()}"

class OutputStage():
    def process(self, data: Any) -> Any:
        return f"Output: {data}"

class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing JSON data through pipeline...")
        print(f"Input: {data}")
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result

class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing CSV data through pipeline...")
        print(f"Input: {data}")
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result

class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        print("Processing Stream data through pipeline...")
        print(f"Input: {data}")
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result

class NexusManager:
    

if __name__ == "__main__":
    data = {"val": 24, "val2": 25}
    # test = TransformStage.process(data)
    json_pipeline = CSVAdapter("JSON_001")
    json_pipeline.add_stages(InputStage())
    json_pipeline.add_stages(TransformStage())
    json_pipeline.add_stages(OutputStage())
    resul = json_pipeline.process(data)
    print(resul)
