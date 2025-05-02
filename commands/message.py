from managers.config import clients
from .command import Command
from managers.clientUtils import *
import managers.db as db

class MessageCommand(Command):
    desired_args = -1
    
    def execute(self, client, args):
        if(client.logged_in == False):
            client.send("ERR_NOAUTH")
            return

        message = " ".join(args)
        broadcast_msg = f"MSG {client.username} {message}"
        broadcast(broadcast_msg, client)
        db.add_message(client.id, message)


