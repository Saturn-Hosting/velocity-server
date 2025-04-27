from managers.config import *
from managers.clientUtils import *

class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.logged_in = False

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
            try:
                message = self.receive()
                if not message:
                    break
                if message.startswith("REGISTER"):
                    parts = message.split()
                    if len(parts) == 3:
                        username, password = parts[1], parts[2]
                        if username in credentials:
                            self.send("ERR_ALREADYREGISTRED\n")
                        else:
                            credentials[username] = password
                            self.send("CONFIRM_REGISTER\n")
                            self.logged_in = True
                    else:
                        self.send("ERR_TOOMANYPARAMS\n")
                else:
                    self.send("ERR_INVALIDCMD\n")
            except Exception as e:
                print(f"Error: {e}")
                break

        self.send("MOTD hello world\n")

        while True:
            try:
                message = self.receive()
                if message:
                    print(f"<{self.addr[0]}> {message}")
                    broadcast(message, self)
                else:
                    remove(self)
                    break
            except Exception as e:
                print(f"Error: {e}")
                break