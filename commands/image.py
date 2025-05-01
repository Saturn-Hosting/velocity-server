from managers.config import credentials, clients
from .command import Command
from managers.clientUtils import *

class ImageCommand(Command):
    desired_args = 1
    
    def execute(self, client, args):
        if(client.logged_in == False):
            client.send("ERR_NOAUTH")
            return

        broadcast_msg = f"IMAGE {client.username} {args[0]}"
        broadcast(broadcast_msg, client)


