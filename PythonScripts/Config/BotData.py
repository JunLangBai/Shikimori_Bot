import json
from wxauto.msgs import FriendMessage
import os

# 初始化全局变量
wxmsgdic = {}

def DefaultBotData():
    data = {
        "group": [],
        "model_list":[],
        "MODEL_NAME":"",
        "SYSTEM_PROMPT":{},
    }
    return data


def GroupData(msg):

    # 步骤 2: 处理消息逻辑
    chat_name = msg.chat_info()["chat_name"]
    if chat_name not in wxmsgdic.keys():
        wxmsgdic[chat_name] = []

    if msg.type == "text":
        chat_content = "[" + msg.sender + "]" + msg.content
        wxmsgdic[chat_name].append(chat_content)
        print("[" + msg.sender + "]" + " " + msg.content)


def LoadConfigData():
    config = None
    if os.path.exists('Json/config.json'):
        with open('Json/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        SaveConfigData(DefaultBotData())
        return DefaultBotData()
    return config

def SaveConfigData(data):
    os.makedirs('Json', exist_ok=True)  # 自动创建目录
    try:
        with open('Json/config.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"配置数据已成功保存到 Json/config.json")
    except (IOError, TypeError) as e:
        print(f"保存配置文件时出错: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

