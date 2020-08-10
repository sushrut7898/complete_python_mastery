from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):  # should define abstract method read || or is considered abstract class will cause error if instanciated without defininf read method
    pass
    # def read(self):
    #   print("Reading data from a memory stream.")


stream = Stream()  # cannot instantiate abstract class
stream.open()

# stream = MemoryStream()
# stream.open()
