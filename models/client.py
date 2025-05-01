from managers.config import config
from managers.clientUtils import broadcast, remove
from managers.commandManager import CommandManager

command_manager = CommandManager()

class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.logged_in = False
        self.username = None

    def send(self, message):
        try:
            self.conn.send(message.encode())
        except Exception as e:
            print(f"Error sending message to {self.addr}: {e}")

    def receive(self):
        try:
            return self.conn.recv(2048).decode().strip()
        except Exception as e:
            print(f"Error receiving message from {self.addr}: {e}")
            return None

    def close(self):
        self.conn.close()

    def thread(self):
        self.send(f"{config['motd']}\n")
        
        while not self.logged_in:
            message = self.receive()
            if not message:
                break
            command_manager.handle(self, message)

        self.send("MOTD hello world\n")

        while True:
            message = self.receive()
            if message:
                print(f"<{self.addr[0]}> {message}")
                command_manager.handle(self, message)
            else:
                remove(self)
                break
