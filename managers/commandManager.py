from commands.command import Command
from commands.register import RegisterCommand
from commands.login import LoginCommand
from commands.message import MessageCommand
from commands.image import ImageCommand
from commands.private_message import PrivateMessageCommand
from commands.ping import PingCommand
from commands.fetch import FetchCommand

class CommandManager:
    def __init__(self): #breaks without the dumb __ shit
        self.commands = {
            'REGISTER': RegisterCommand(),
            'LOGIN': LoginCommand(),
            'MSG': MessageCommand(),
            'IMAGE': ImageCommand(),
            'PRIVMSG':  PrivateMessageCommand(),
            'PING': PingCommand(),
            'FETCH': FetchCommand()
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
            if len(args) != command.desired_args and len(args) != -1:
                if(len(args) > command.desired_args): client.send("ERR_TOOMANYPARAMS\n")
                else: client.send("ERR_NEEDMOREPARAMS\n")
                return
            else: command.execute(client, args)
        else:
            client.send("ERR_INVALIDCMD\n")
