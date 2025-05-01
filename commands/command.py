class Command: #base class for commands
    def execute(self, client, args):
        raise NotImplementedError("Execute method isn't implemented!")
