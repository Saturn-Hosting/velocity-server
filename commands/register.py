from managers.config import credentials
from .command import Command

class RegisterCommand(Command):
    desired_args = 2

    def execute(self, client, args):        
        username, password = args
        if username in credentials:
            client.send("ERR_ALREADYREGISTRED\n")
        else:
            credentials[username] = password
            client.send("CONFIRM_REGISTER\n")
            client.username = username
            client.logged_in = True
