import sys
import importlib
import time
from pathlib import Path

from PythonScripts.Command.Command import Command
from PythonScripts.Command import *

class CommandEngine:
    def __init__(self):
        live =  AliveCommand()
        sign = AISignCommand()
        chat = AIChatCommand()
        self.commands = {}
        self._import_command_modules()
        self._discover_commands()

    def _is_chinese_char(self, char):
        """检查字符是否是汉字"""
        return '\u4e00' <= char <= '\u9fff'

    #严格匹配
    def _match_strict_command(self, content, command_name):
        return content == command_name

    #宽松匹配
    def _match_loose_command(self, content, command_name):
        return command_name in content

    def _import_command_modules(self):
        """动态导入所有命令模块"""
        print("开始导入命令模块...")

        # 获取当前文件所在目录的父目录
        base_dir = Path(__file__).parent.parent

        # 命令模块所在的目录
        commands_dir = base_dir / "Command"
        print(f"命令目录: {commands_dir}")

        # 检查目录是否存在
        if not commands_dir.exists():
            print(f"错误: 命令目录不存在 - {commands_dir}")
            return

        # 遍历目录中的所有 Python 文件
        for file in commands_dir.glob("*.py"):
            # 跳过 __init__.py 和 Command.py
            if file.name.startswith("__") or file.name == "Command.py":
                continue

            # 构建模块路径
            module_name = f"PythonScripts.Command.{file.stem}"
            print(f"尝试导入模块: {module_name}")

            try:
                # 检查是否已导入
                if module_name in sys.modules:
                    print(f"  模块已导入，跳过")
                    continue

                # 导入模块
                importlib.import_module(module_name)
                print(f"成功导入模块: {module_name}")
            except Exception as e:
                print(f"导入模块失败: {module_name} - {e}")

    def _discover_commands(self):
        print("开始发现命令...")
        """自动发现并注册所有命令子类及其别名"""
        command_classes = self._get_all_subclasses(Command.Command)
        print(f"发现 {len(command_classes)} 个命令类")

        if not command_classes:
            print("警告: 没有找到任何命令类")
            return

        for cmd_class in command_classes:
            if cmd_class is Command:
                continue

            print(f"处理命令类: {cmd_class.__name__}")
            cmd_instance = cmd_class()

            # 获取命令的所有触发名称
            names = set()

            # 1. 添加类名（小写）
            names.add(cmd_class.__name__.lower())

            # 2. 添加别名数组中所有名称（小写）
            aliases = getattr(cmd_class, 'aliases', [])
            print(f"  别名: {aliases}")
            for alias in aliases:
                names.add(alias.lower())

            # 注册所有触发名称
            for name in names:
                if name in self.commands:
                    print(f"警告: 命令名 '{name}' 已存在，将被覆盖")
                self.commands[name] = cmd_instance
                print(f"注册命令: {name} -> {type(cmd_instance).__name__}")

    def _get_all_subclasses(self, cls):
        """递归获取所有子类"""
        subclasses = []
        for subclass in cls.__subclasses__():
            subclasses.append(subclass)
            subclasses.extend(self._get_all_subclasses(subclass))
        return subclasses

    def execute_command(self, msg, chat):
        """执行指定命令"""
        content = msg.content.strip()
        if not content:
            return False

        # 检查第一个字符是否是汉字
        if not self._is_chinese_char(content[0]):
            return False

        # 遍历所有注册的命令
        for command_name, command_instance in self.commands.items():
            # 根据命令的 strict 属性选择匹配模式
            if command_instance.strict:
                matched = self._match_strict_command(content, command_name)
            else:
                matched = self._match_loose_command(content, command_name)

            if matched:
                print(f"执行命令: {command_name} (strict={command_instance.strict})")
                try:
                    time.sleep(0.5)
                    command_instance.execute(msg, chat)
                    return True
                except Exception as e:
                    print(f"命令执行出错: {e}")
                    return False

        print(f"未匹配到任何命令: {content}")  # 未找到指令，则执行普通聊天
        # AIchat = AIChatCommand()
        # AIchat.execute(msg=msg, chat=chat)
        return False