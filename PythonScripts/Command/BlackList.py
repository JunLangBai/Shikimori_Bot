from PythonScripts.Command.Command import Command
from PythonScripts.Config.BotData import LoadConfigData

class BlackList(Command):
    aliases = ["黑名单"]
    strict = True

    def __init__(self):
        self.config = LoadConfigData()
        self.blacklist = self.config.setdefault("BLACKLIST", [])

    def execute(self, msg, chat, cmd):

        chat_name = msg.chat_info()['chat_name']

        # 显示帮助信息：写查看
        if not self.blacklist:
            chat.SendMsg("黑名单列表为空", who=chat_name)
        else:
            user_list = "\n".join([f"• @{uid}" for uid in self.blacklist])
            chat.SendMsg(f" 黑名单列表:\n{user_list}", who=chat_name)



    def extract_user_id(self, user_str):
        """从消息中提取用户ID"""
        return user_str.strip().lstrip('@').strip()

