import json
from wxauto.msgs import FriendMessage

# 初始化全局变量
wxmsgdic = {}

def DefaultBotData():
    data = {
        "group": group_value
    }
    return data

# def _load_json_to_wxmsgdic(file_path):
#     """
#     从指定的 JSON 文件加载数据到 wxmsgdic。
#     如果文件不存在或为空，则初始化为空字典。
#     """
#     global wxmsgdic
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             wxmsgdic = json.load(file)
#     except FileNotFoundError:
#         print(f"文件 {file_path} 未找到，初始化为空字典。")
#         wxmsgdic = {}
#     except json.JSONDecodeError:
#         print(f"文件 {file_path} 内容无效，初始化为空字典。")
#         wxmsgdic = {}
#
# def _save_wxmsgdic_to_json(file_path):
#     """
#     将 wxmsgdic 的内容保存为 JSON 文件。
#     """
#     global wxmsgdic
#     try:
#         with open(file_path, 'w', encoding='utf-8') as file:
#             json.dump(wxmsgdic, file, ensure_ascii=False, indent=4)
#         print(f"数据已成功保存到 {file_path}")
#     except Exception as e:
#         print(f"保存数据到 {file_path} 失败: {e}")

def GroupData(msg, json_file_path):
    """
    处理群消息并将 wxmsgdic 的内容保存为 JSON 格式。
    """
    # global wxmsgdic
    #
    # # 步骤 1: 加载 JSON 数据到 wxmsgdic
    # _load_json_to_wxmsgdic(json_file_path)

    # 步骤 2: 处理消息逻辑
    chat_name = msg.chat_info()["chat_name"]
    if chat_name not in wxmsgdic.keys():
        wxmsgdic[chat_name] = []

    if isinstance(msg, FriendMessage):
        chat_content = "[" + msg.sender + "]" + msg.content
        wxmsgdic[chat_name].append(chat_content)
        print("[" + msg.sender + "]" + " " + msg.content)

    # # 步骤 3: 保存 wxmsgdic 到 JSON 文件
    # _save_wxmsgdic_to_json(json_file_path)

def LoadConfigData():
    config = None
    if os.path.exists('Json/config.json'):
        with open('Json/config.json', 'r') as f:
            config = json.load(f)
    else:
        SaveConfigData(DefaultBotData())
    return config

def SaveConfigData(data):
    try:
        with open('Json/config.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"配置数据已成功保存到 {filename}")
    except (IOError, TypeError) as e:
        print(f"保存配置文件时出错: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

