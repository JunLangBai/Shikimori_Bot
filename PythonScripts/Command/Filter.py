from PythonScripts.Command.Command import Command
from PythonScripts.Config.BotData import LoadConfigData, SaveConfigData

class Filter(Command):
    aliases = ["过滤词"]
    strict = True

    def __init__(self):
        self.config = LoadConfigData()
        self.filter_words = self.config.setdefault("FILTER_WORDS", [])

    def execute(self, msg, chat, cmd):

        chat_name = msg.chat_info()['chat_name']

        # 显示帮助信息：写查看
        if not self.filter_words:
            chat.SendMsg("过滤词列表为空", who=chat_name)
        else:
            word_list = "\n".join([f"• {word}" for word in self.filter_words])
            chat.SendMsg(f"过滤词列表:\n{word_list}", who=chat_name)