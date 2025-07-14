from PythonScripts.Command.Command import Command
from PythonScripts.Config.BotConfig import *
from PythonScripts.libraries.AIChat.AIChat import *

class AISignCommand(Command):
    aliases = ['打卡']
    strict = False

    def execute(self, msg, chat):
        chat.SendMsg(msg="签到成功！", who=msg.chat_info()['chat_name'], clear=True)# 宽松匹配模式




