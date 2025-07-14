from abc import ABC, abstractmethod


# 抽象命令基类
class Command(ABC):
    # 命令别名数组，子类可覆盖此属性
    aliases = []
    strict = True

    @abstractmethod
    def execute(self,msg,chat):
        """子类必须实现此方法"""
