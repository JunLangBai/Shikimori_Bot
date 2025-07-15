import sys
import time
import os  # 添加缺失的导入

from PythonScripts.Config.BotData import *

class CmdEngine:
    config = LoadConfigData()

    def clear_console(self):
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # macOS/Linux
            os.system('clear')

    def addgroup(self):
        a = str(input("输入你要监听的群组名称（必须与微信群名一致！）"))
        if "group" not in self.config:
            self.config["group"] = []  # 若键不存在，创建空列表
        elif not isinstance(self.config["group"], list):
            self.config["group"] = [self.config["group"]]  # 将现有值转换为列表
        if a not in self.config["group"]:
            self.config["group"].append(a)
        else:
            print(f"群组 '{a}' 已存在，未添加重复项")
            return
        SaveConfigData(self.config)
        print("完成添加！即将返回配置菜单...")
        time.sleep(1)
        return

    def delgroup(self):
        print("\n当前监听群组:")
        for i, group in enumerate(self.config.get("group", []), 1):
            print(f"{i}. {group}")
        if not self.config["group"]:
            print("没有可删除的群组")
            return
        try:
            index = int(input("输入要删除的群组编号: ")) - 1
            if 0 <= index < len(self.config["group"]):
                removed = self.config["group"].pop(index)
                SaveConfigData(self.config)
                print(f"已删除群组: {removed}")
            else:
                print("无效的编号")
                return
        except ValueError:
            print("无效指令！\n")
            return


    def changegroupconfig(self):
        self.clear_console()

        groups = self.config.get("group", [])
        print("\n当前监听群组:")
        for i, group in enumerate(groups, 1):
            print(f"{i}. {group}")

        while True:
            self.clear_console()
            print("\n操作选项:")
            print("1. 添加群组")
            print("2. 删除群组")
            try:
                choice = int(input("请选择操作: "))
                if choice == 1:
                    self.addgroup()
                if choice == 2:
                    self.delgroup()
            except ValueError:
                print("无效指令！\n")
                return


    def configmenu(self):
        while True:
            self.clear_console()
            self._display_configmenu()
            try:
                cmd = int(input("输入数字并按下回车进行相应命令： "))
                if cmd == 1:
                    self.changegroupconfig()
                else:
                    continue
            except ValueError:
                print("无效指令！\n")
                return

    def mainmenu(self):
        while True:
            self.clear_console()
            # 显示菜单
            self._display_menu()
            try:
                cmd = int(input("输入数字并按下回车进行相应命令： "))
                if cmd == 1:
                    self.clear_console()
                    break
                if cmd == 2:
                    self.configmenu()
                if cmd == 3:
                    sys.exit(0)
                else:
                    continue
            except ValueError:
                print("无效指令！\n")
                continue


    def _display_menu(self):
        print("=" * 20)
        print("     菜单选项")
        print("=" * 20)
        print("1. 开始运行")
        print("2. 修改配置")
        print("3. 退出应用")
        print("=" * 20)

    def _display_configmenu(self):
        print("=" * 20)
        print("     菜单选项")
        print("=" * 20)
        print("1.修改监听群组列表")
        print("2.修改本地模型")
        print("3.修改模型人设")
        print("=" * 20)



