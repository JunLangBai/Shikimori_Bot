from PythonScripts.Command.Command import Command
import json
import os
from datetime import datetime
from PythonScripts.Config.BotConfig import *

TRIGGER_WORDS = TRIGGER_WORDS

class AISignCommand(Command):
    aliases = ['打卡']


    # 金币数据存储路径
    GOLD_DATA_FILE = "Json/gold_data.json"

    def __init__(self):
        super().__init__()
        # 加载已有的金币数据
        self.gold_data = self.load_gold_data()

    def load_gold_data(self):
        """从JSON文件加载金币数据"""
        if os.path.exists(self.GOLD_DATA_FILE):
            try:
                with open(self.GOLD_DATA_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_gold_data(self):
        """保存金币数据到JSON文件"""
        with open(self.GOLD_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.gold_data, f, ensure_ascii=False, indent=2)

    def get_today_date(self):
        """获取当前日期字符串（格式YYYYMMDD）"""
        return datetime.now().strftime("%Y%m%d")

    def execute(self, msg, chat):
        print(msg)
        chat_id = msg.sender
        user_id = msg.id
        today = self.get_today_date()

        # 初始化群组数据
        if chat_id not in self.gold_data:
            self.gold_data[chat_id] = {
                "users": {},
                "last_sign_date": {}  # 记录用户最后签到日期
            }

        group_data = self.gold_data[chat_id]
        last_sign = group_data["last_sign_date"].get(chat_id, "")

        # 检查今日是否已签到
        if last_sign == today:
            chat.SendMsg(msg="您今天已经签到过了，请明天再来！",
                         who=msg.chat_info()['chat_name'])
            return

        # 更新签到状态
        group_data["last_sign_date"][chat_id] = today

        # 更新金币数量
        user_gold = group_data["users"].get(chat_id, 0)
        new_gold = user_gold + 5
        group_data["users"][chat_id] = new_gold

        # 保存数据
        self.save_gold_data()
        import time
        # 发送响应
        response = (
            f"{chat_id} 签到成功！\n"
            f"获得金币：5枚\n"
            f"当前金币：{new_gold}枚\n"
            f"签到时间：{time.strftime("%Y-%m-%d", time.localtime())}\n"
            f"积累100金币可以跟群主兑换战斗通行证哦~\n"
            f"式守陪伴你每一天 ❤"
        )
        chat.SendMsg(msg=response,
                     who=msg.chat_info()['chat_name'])








