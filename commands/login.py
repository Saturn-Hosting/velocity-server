from .command import Command
import managers.db as db

class LoginCommand(Command):
    desired_args = 2
    
    def execute(self, client, args):
        username, password = args
        user = db.get_user(username)
        if not user:
            client.send("ERR_INVALIDCREDENTIALS")
            return

        if db.verify_password(username, password) is False:
            client.send("ERR_INVALIDCREDENTIALS")
            return

        else:
            client.username = username
            client.send("CONFIRM_LOGIN")
            client.logged_in = True
            client.id = user['id']
