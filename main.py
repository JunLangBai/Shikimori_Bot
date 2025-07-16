from wxauto import WeChat
from wxauto.msgs import FriendMessage
import time
import json
from PythonScripts.Config.BotData import GroupData
from pathlib import Path

from PythonScripts.libraries.AIChat.AIChat import *
from PythonScripts.Engine.CmdEngine import *

from PythonScripts.libraries.AIChat.RandomReply import  *


init = CmdEngine().mainmenu()

from PythonScripts.Engine.CommandEngine import CommandEngine

wx = WeChat()
engine = CommandEngine()

script_dir = Path(__file__).resolve().parent
json_path = "Json/ BotData.json"
#
# # 获取文件夹路径（即 Json 文件所在的目录）
# folder_path = json_path.parent
#
# t = time.time()
#
# # 检查文件夹是否存在，如果不存在则创建
# if not folder_path.exists():
#     folder_path.mkdir(parents=True, exist_ok=True)
#     print(f"文件夹已创建: {folder_path}")
# else:
#     print(f"文件夹已存在: {folder_path}")


# 消息处理函数
def on_message(msg, chat):
    global t
    GroupData(msg,json_path)
    if isinstance(msg, FriendMessage):
        engine.execute_command(msg,chat)
        # t = 0
        # t = time.time()

    # if t > 30:
    #     t = 0
    #     t = time.time()
    #     sim = RandomReply(msg.chat_info()['chat_name'],"式守请按群冷场的场景去开始对话")
    #     engine.execute_command(sim,chat)

print("余小宁")

wx.AddListenChat(nickname="傻逼机器测试群", callback=on_message)

# 保持程序运行
wx.KeepRunning()
