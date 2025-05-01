from .command import Command
import managers.db as db

class RegisterCommand(Command):
    desired_args = 2

    def execute(self, client, args):        
        username, password = args
        user = db.get_user(username)
        if user:
            client.send("ERR_ALREADYREGISTRED\n")
        else:
            db.add_user(username, password)
            client.send("CONFIRM_REGISTER\n")
            client.username = username
            client.id = db.get_user(username).id
            client.logged_in = True
