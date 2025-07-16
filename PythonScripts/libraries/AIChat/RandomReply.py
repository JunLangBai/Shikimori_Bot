class RandomReply:
    def __init__(self,chat_name,content):
        self.content = content
        self.chat_name = chat_name

    def chat_info(self):
        return {"chat_name": self.chat_name}