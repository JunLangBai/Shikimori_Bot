from wxauto import WeChat
from wxauto.msgs import FriendMessage
import time
import json
from Config.BotData import GroupData
from pathlib import Path

from PythonScripts.Engine.CommandEngine import CommandEngine

wx = WeChat()
engine = CommandEngine()

script_dir = Path(__file__).resolve().parent
json_path = script_dir / "Json" / "BotData.json"

# 获取文件夹路径（即 Json 文件所在的目录）
folder_path = json_path.parent

# 检查文件夹是否存在，如果不存在则创建
if not folder_path.exists():
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"文件夹已创建: {folder_path}")
else:
    print(f"文件夹已存在: {folder_path}")


# 获取当前脚本所在目录

# 消息处理函数
def on_message(msg, chat):
    GroupData(msg,json_path)
    if isinstance(msg, FriendMessage):
        engine.execute_command(msg,chat)

wx.AddListenChat(nickname="傻逼机器测试群", callback=on_message)

# 保持程序运行
wx.KeepRunning()
