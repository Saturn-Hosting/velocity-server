from managers.config import credentials
from .command import Command

class LoginCommand(Command):
    desired_args = 2
    
    def execute(self, client, args):
        username, password = args
        if username not in credentials:
            client.send("ERR_INVALIDCREDENTIALS\n")
            return

        if password != credentials[username]:
            client.send("ERR_INVALIDCREDENTIALS\n")
            return

        else:
            client.username = username
            client.send("CONFIRM_LOGIN\n")
            client.logged_in = True
