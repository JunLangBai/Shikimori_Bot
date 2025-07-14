
import time
import threading
from collections import deque
from openai import OpenAI
from PythonScripts.Command.AIChatCommand import TRIGGER_WORDS, STRICT_MODE
from PythonScripts.Config.BotConfig import OLLAMA_BASE_URL, OLLAMA_API_KEY, MODEL_NAME, SYSTEM_PROMPT

class AIChatCommand:
    # 使用外部配置
    aliases = TRIGGER_WORDS
    strict = STRICT_MODE

    def __init__(self):
        # 初始化OpenAI客户端
        self.client = OpenAI(
            base_url=OLLAMA_BASE_URL,
            api_key=OLLAMA_API_KEY,
        )

        # 历史记录管理
        self.history = {}
        self.lock = threading.Lock()

    def get_history(self, chat_name):
        """获取或创建聊天历史记录"""
        with self.lock:
            if chat_name not in self.history:
                self.history[chat_name] = deque(maxlen=10)
            return self.history[chat_name]

    def clear_history(self, chat_name):
        """清空聊天历史记录"""
        with self.lock:
            if chat_name in self.history:
                self.history[chat_name].clear()
                return True
            return False

    def execute(self, msg, chat):
        """执行AI聊天命令"""
        content = msg.content.strip()
        chat_name = msg.chat_info()['chat_name']

        # 检查清空命令
        if "清空历史" in content:
            if self.clear_history(chat_name):
                chat.SendMsg("已清空聊天历史", who=chat_name)
            else:
                chat.SendMsg("没有历史可清空", who=chat_name)
            return

        # 获取历史记录
        history = self.get_history(chat_name)

        # 添加用户消息到历史
        history.append({"role": "user", "content": content})

        try:
            # 准备完整上下文
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            messages.extend(list(history))

            # 调用AI模型
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.7
            )

            # 获取回复内容
            reply = response.choices[0].message.content

            # 添加AI回复到历史
            history.append({"role": "assistant", "content": reply})

            # 发送回复
            chat.SendMsg(reply, who=chat_name)

        except Exception as e:
            chat.SendMsg(f"出错了: {str(e)}", who=chat_name)