from src.connection.connection import AConnection


class WebSocketConnection(AConnection):
    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

    def send(self, data: bytes) -> None:
        pass

    def receive(self, amount: int) -> bytes:
        pass
