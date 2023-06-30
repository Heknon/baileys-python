import abc
from typing import Self


class AConnection(metaclass=abc.ABCMeta):
    """
    A Base Abstract class representing a connection to a data stream
    This connection can be sent data to and receive data as well
    """

    @abc.abstractmethod
    def open(self) -> None:
        """
        Open the connection - initiate the connection
        :raises ConnectionError: opening the connection fails
        """

    @abc.abstractmethod
    def close(self) -> None:
        """
        Close the currently active connection
        :raises ConnectionError: closing the connection fails
        """

    @abc.abstractmethod
    def send(self, data: bytes) -> None:
        """
        receive data from the connection
        :param data: the data to send
        :raises ConnectionError: if sending the data fails
        """

    @abc.abstractmethod
    def receive(self, amount: int) -> bytes:
        """
        receive data from the connection
        :param amount: the maximum amount of data to receive
        :raises ConnectionError: if receiving fails
        :return: the data received
        """

    def __enter__(self) -> Self:
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False
