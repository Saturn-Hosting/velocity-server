from .command import Command
import managers.db as db

class MessageCommand(Command):
    desired_args = 1

    def execute(self, client, args):
        if len(args) < 1:
            client.send("ERR_NEEDMOREPARAMS")
            return
        
        index = int(args[0])
        messages = db.fetch_messages(index)
        if messages:
            for message in messages:
                sender = db.get_user_by_id(message[1])
                client.send(f"FETCH {message[3]} {sender.username} {message[2]}")
        else:
            client.send("ERR_NOMESSAGES")