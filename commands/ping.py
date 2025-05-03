from .command import Command
from managers.clientUtils import *

class PingCommand(Command):
    desired_args = 1
    
    def execute(self, client, args):
        if len(args) < 1:
            client.send("ERR_NEEDMOREPARAMS")
            return

        if args[0] != "912389":
            return
        
        client.send("PONG 912389")
