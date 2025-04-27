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