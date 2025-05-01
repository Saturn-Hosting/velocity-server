from commands.command import Command
from commands.register import RegisterCommand
from commands.login import LoginCommand

class CommandManager:
    def __init__(self): #breaks without the dumb __ shit
        self.commands = {
            'REGISTER': RegisterCommand(),
            'LOGIN': LoginCommand(),
        }

    def handle(self, client, message):
        parts = message.split()
        if not parts:
            client.send("ERR_INVALIDCMD\n")
            return

        cmd_name = parts[0].upper()
        args = parts[1:]

        command = self.commands.get(cmd_name)
        if command:
            if len(args) != command.desired_args:
                if(len(args) > command.desired_args): client.send("ERR_TOOMANYPARAMS\n")
                else: client.send("ERR_NEEDMOREPARAMS\n")
                return
            else: command.execute(client, args)
        else:
            client.send("ERR_INVALIDCMD\n")
