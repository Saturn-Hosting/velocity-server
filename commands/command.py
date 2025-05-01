class Command: #base class for commands
    desired_args = 0
    
    def execute(self, client, args):
        raise NotImplementedError("Execute method isn't implemented!")
