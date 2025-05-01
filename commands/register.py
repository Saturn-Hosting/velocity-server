from managers.config import credentials
from .command import Command

class RegisterCommand(Command):
    def execute(self, client, args):
        if len(args) != 2:
            client.send("ERR_TOOMANYPARAMS\n")
            return
        
        username, password = args
        if username in credentials:
            client.send("ERR_ALREADYREGISTRED\n")
        else:
            credentials[username] = password
            client.send("CONFIRM_REGISTER\n")
            client.logged_in = True
