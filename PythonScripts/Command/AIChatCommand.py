from PythonScripts.Command.Command import Command

class AIChatCommand(Command):
    aliases = ["式守"]

    def execute(self,msg,chat):
        chat.SendMsg(msg="也活着", who=msg.chat_info()['chat_name'], clear=True)# 宽松匹配模式