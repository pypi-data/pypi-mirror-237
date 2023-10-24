from redstat.output.base import Output
from redstat.functions.save import save_json


class ConsoleOutput(Output):
    @staticmethod
    def output(namespace, data: list):
        for i in data:
            print(i)


class FileOutput(Output):
    @staticmethod
    def output(namespace, data: list):
        stream = namespace.output
        save_json(stream, data)
