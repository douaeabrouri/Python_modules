#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, result: str)  -> str:
        return f"Output: {result}"

class NumericProcessor(DataProcessor):
    """Check if data is a list of numbers"""
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(i, (int, float)) for i in data)
    """Process numeric data - calculate sum and average"""
    def process(self, data: Any) -> str:
        try:
            if isinstance(data, list) == True:
               lenght: int = len(data)
               somme: int = sum(data) 
               avg: float = somme/lenght
               return f"Processed {lenght} numeric values, sum={somme}, avg={avg}"
        except Exception as e:
            return f"ERROR: processing numeric data: {str(e)}"
        
class TextProcessor(DataProcessor):
    """Check if data is a string"""
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)
    """Process text data - count characters and words"""
    def process(self, data: Any) -> str:
        try:
            if isinstance(data, str) == True:
               len_char: int = len(data) 
               len_words: int = len(data.split())
               return f"Processed text: {len_char} characters, {len_words} words"
        
        except Exception as e:
            return f"ERROR: processing text data: {str(e)}"
        
class LogProcessor(DataProcessor):
    """Check if data is a string that looks like a log entry"""
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ': ' in data
    
    def process(self, data: Any) -> str:
        liste: list = data.split(':', 1)
        level: str = liste[0]
        message: str = liste[1]
        prefix: str = ""
        if level == "ERROR":
            prefix = "[ALERT]"
        else:
            prefix = f"[{level}]"
        return f"{prefix} {level} level detected: {message}"

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    
    print("Initializing Numeric Processor...")
    num_processor = NumericProcessor()
    
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_data: list = [1, 2, 3, 4, 5]
    if num_processor.validate(numeric_data):
       print("Validation: Numeric data verified")
       result = num_processor.process(numeric_data)
       print(f"Output: {result}\n")
    print("Initializing Text Processor...")
    text_processor = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    text_data: str = "Hello Nexus World"
    if text_processor.validate(text_data):
        print("Validation: Text data verified")
        result = text_processor.process(text_data)
        print(f"Output: {result}\n")
        print("Initializing Log Processor...")
    log_processor = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    log_data = "ERROR: Connection timeout"
    if log_processor.validate(log_data):
        print("Validation: Log entry verified")
        result = log_processor.process(log_data)
        print(f"Output: {result}")
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    test_cases: dict = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World"),
        (LogProcessor(), "INFO: System ready")
    ]
    for i, (processor, data) in enumerate(test_cases, 1):
        result = processor.process(data)
        print(f"Result {i}: {result}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")