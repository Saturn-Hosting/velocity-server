from managers.config import credentials, clients
from .command import Command
from managers.clientUtils import *

class MessageCommand(Command):
    desired_args = -1
    
    def execute(self, client, args):
        if(client.logged_in == False):
            client.send("ERR_NOAUTH")
            return

        if len(args) < 2:
            client.send("ERR_NEEDMOREPARAMS")
            return

        message = " ".join(args)
        broadcast_msg = f"MSG {client.username} {message}"
        broadcast(broadcast_msg, client)


