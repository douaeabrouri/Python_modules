#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str, type: str):
        self.stream_id = stream_id
        self.type = type
        self.processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]= None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
               "stream_id": self.stream_id,
               "type": self.type,
               "processed": self.processed
        }

class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            values: list[float] = [float(item.split(':')[1]) for item in data_batch]
            somme: float = sum(values)
            lenght: float = len(data_batch)
            avg: float = somme / lenght
            return f"Sensor analysis: {lenght} readings processed, avg temp: {avg}°C"
        except Exception as e:
            return f"ERROR: {e}"
class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id,  "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            lenght: int = len(data_batch)
            val: float = 0
            for item in data_batch:
                parts: list[str] = item.split(':')
                operation: str = parts[0]
                value: float = float(parts[1])
                if operation == "buy":
                   val += value
                else:
                   val -= value
            return f"Transaction analysis: {lenght} operations, net flow: +{val} units"
        except Exception as e:
            return f"ERROR: {e}"
class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            lenght: int = len(data_batch)
            errornub: int = data_batch.count("error")
            return f"Event analysis: {lenght} events, {errornub} errors detected"
        except Exception as e:
            return f"ERROR : {e}"

class StreamProcessor:
    def __init__(self) -> None:
        pass
    def add_stream(self, stream: DataStream) -> None:
        pass
    def process_all(self, data_bach: List[Any]) -> None:
        pass 

if __name__ == "__main__":
    obj = SensorStream()
    data_batch = ["first:20", "temp:30.2"]
    string = obj.process_batch(data_batch)
    print(string)
    