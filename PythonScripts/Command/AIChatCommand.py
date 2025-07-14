from PythonScripts.Command.Command import Command
from PythonScripts.libraries.AIChat.AIChat import *


class AliveCommand(Command):
    strict = False
    aliases = ["式守"]

    def execute(self, msg, chat):
        AIchat = AIChatCommand()
        AIchat.execute(msg=msg, chat=chat)