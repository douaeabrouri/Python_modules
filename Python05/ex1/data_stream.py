#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str, processed: int):
        self.stream_id = stream_id
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
               "processed": self.processed
        }
    class SensorStream:
        pass
    class TransactionStream:
        pass
    class EventStream:
        pass


class StreamProcessor:

    data_batch: list = ["temp:20", "humidity:60", "temp:30"]
    streams: list = ["SensorStream, TransactionStream, EventStream"]
    def __init__(self, streams: list):
        self.streams = streams
    

    # def process_batch(self, data_batch: List[Any]) -> str:
    #     try:
    #         filterd: list = self.filter_data(data_batch, "temp")
    #         somme: float = [float(item.split(':')[1]) for item in filterd]
    #         lenght: float = len(filterd)
    #         avg: float = somme / lenght
    #         print(f"Sensor analysis: {lenght} readings processed, avg temp: {avg}°C")
    #     except Exception as e:
    #         print(f"ERROR: {e}")
