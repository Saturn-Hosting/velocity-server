from managers.config import credentials, clients
from .command import Command
from managers.clientUtils import *
import managers.db as db

class PrivateMessageCommand(Command):
    desired_args = -1
    
    def execute(self, client, args):
        if not client.logged_in:
            client.send("ERR_NOAUTH")
            return

        if len(args) < 2:
            client.send("ERR_NEEDMOREPARAMS")
            return

        recipient_username = args[0]
        message = " ".join(args[1:])

        private_msg = f"PRIVMSG {client.username} {message}"
        success = private_broadcast(recipient_username, private_msg, client)
        
        if not success:
            client.send("ERR_NOSUCHUSER")
        
        recipient = db.get_user(recipient_username)
        db.add_private_message(client.id, recipient.id, message)