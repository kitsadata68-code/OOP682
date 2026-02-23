import csv
from abc import ABC, abstractmethod

class IlogSource(ABC):
    @abstractmethod
    def get_logs(self):
        pass

class FilelogSource(IlogSource):
    def get_logs(self):
        return["Log from text file 1", "Log from text file 2"]
    
class MainWindow:
    def __init__(self, source: IlogSource):
        self.source = source

    def display_logs(self):
        logs = self.source.get_logs()
        for log in logs:
            print(log)

class CsvLogSource(IlogSource):
    def __init__(self, filename):
        self.filename = filename

    def get_logs(self):
        logs = []
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    logs.append(f"CSV Log: {row}")
        except FileNotFoundError:
            logs.append("Error: File not found.")
        return logs