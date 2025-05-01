from managers.config import credentials
from .command import Command

class LoginCommand(Command):
    def execute(self, client, args):
        if len(args) != 2:
            client.send("ERR_TOOMANYPARAMS\n")
            return
        
        username, password = args
        if username not in credentials:
            client.send("ERR_INVALIDCREDENTIALS\n")
            return

        if password != credentials[username]:
            client.send("ERR_INVALIDCREDENTIALS\n")
            return
            
        else:
            client.send("CONFIRM_LOGIN\n")
            client.logged_in = True
