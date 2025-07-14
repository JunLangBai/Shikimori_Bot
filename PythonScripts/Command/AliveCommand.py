from PythonScripts.Command.Command import Command


class AliveCommand(Command):
    aliases = ["存活确认", "确认存活"]

    def execute(self,msg,chat):
        chat.SendMsg(msg="也活着", who=msg.chat_info()['chat_name'], clear=True)
