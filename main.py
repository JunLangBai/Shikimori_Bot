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

config_path = LoadConfigData()

# 消息处理函数
def on_message(msg, chat):
    GroupData(msg)
    if isinstance(msg, FriendMessage):
        engine.execute_command(msg,chat)
        # t = 0
        # t = time.time()

    # if t > 30:
    #     t = 0
    #     t = time.time()
    #     sim = RandomReply(msg.chat_info()['chat_name'],"式守请按群冷场的场景去开始对话")
    #     engine.execute_command(sim,chat)

for i in config_path["group"]:
    wx.AddListenChat(nickname=i, callback=on_message)

# 保持程序运行
wx.KeepRunning()
