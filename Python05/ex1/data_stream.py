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
            self.processed += lenght
            return f"Transaction analysis: {lenght} operations, net flow: +{val} units"
        except Exception as e:
            return f"ERROR: {e}"
class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            lenght: int = len(data_batch)
            errornub: int = sum(1 for item in data_batch if "error" in item)
            self.processed += 1
            return f"Event analysis: {lenght} events, {errornub} errors detected"
        except Exception as e:
            return f"ERROR : {e}"

class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)
    def process_all(self, data_batch: List[Any]) -> None:
        for stream in self.streams:
            result = stream.process_batch(data_batch)
            print(result)

if __name__ == "__main__":

    print("=== CODE NEXUS DATA STREAM SYSTEM ===")

    sensor = SensorStream("sensor_1")
    transactions = TransactionStream("tx_1")
    events = EventStream("event_1")

    processor = StreamProcessor()

    processor.add_stream(sensor)
    processor.add_stream(transactions)
    processor.add_stream(events)

    sensor_data = ["temp:20", "temp:30", "temp:25"]
    transaction_data = ["buy:100", "sell:40", "buy:10"]
    event_data = ["info:start", "error:disk", "error:network"]

    print(sensor.process_batch(sensor_data))
    print(transactions.process_batch(transaction_data))
    print(events.process_batch(event_data))
    