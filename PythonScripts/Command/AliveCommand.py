from PythonScripts.Command.Command import Command


class AliveCommand(Command):

    aliases = ["存活确认", "确认存活","存活"]

    def execute(self, msg, chat):
        print("get")
        chat.SendMsg(msg="收到，式守当然在啦❤", who=msg.chat_info()['chat_name'], clear=True)
