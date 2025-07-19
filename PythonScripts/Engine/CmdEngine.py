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

    def has_empty_value(self,data):
        # 处理字典类型
        if isinstance(data, dict):
            # 检查字典自身是否为空
            if not data:
                return True
            # 递归检查所有值
            for value in data.values():
                if self.has_empty_value(value):
                    return True
        # 处理列表类型
        elif isinstance(data, list):
            # 检查列表是否为空或包含空值
            if not data:  # 空列表 [] 被视为空值
                return True
            for item in data:
                if self.has_empty_value(item):
                    return True
        # 处理基本数据类型
        elif data is None or data == "":
            return True
        return False


    def addgroup(self):
        a = str(input("输入你要监听的群组名称（必须与微信群名一致！）"))
        print()
        print("若要返回请按下[Q]")
        # 允许输入"q"退出
        if a.lower() == 'q':
            print("操作取消")
            return
        if "group" not in self.config:
            self.config["group"] = []
            SaveConfigData(self.config["group"])  # 若键不存在，创建空列表
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
        if "group" not in self.config:
            self.config["group"] = []
            SaveConfigData(self.config)
        print("\n当前监听群组:")
        for i, group in enumerate(self.config.get("group", []), 1):
            print(f"{i}. {group}")
            print()
            print("若要返回请按下[Q]")
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
                print("无效的编号\n")
                return
        except ValueError:
            print("无效指令！\n")
            return

    def chosemodel(self):
        print("\n当前模型:")
        if "model_list" not in self.config:
            self.config["model_list"] = []
        for i, model in enumerate(self.config.get("model_list", []), 1):
            print(f"{i}. {model}")
        if not self.config["model_list"]:
            print("没有可用的模型")
            return
        try:
            index = int(input("输入要选择的模型编号: ")) - 1
            if 0 <= index < len(self.config["model_list"]):
                if "MODEL_NAME" not in self.config:
                    self.config["MODEL_NAME"] = ""
                self.config["MODEL_NAME"] = self.config["model_list"][index]
                SaveConfigData(self.config)
                print(f"已选择模型: {self.config["model_list"][index]}")
            else:
                print("无效的编号\n")
                return
        except ValueError:
            print("无效指令！\n")
            return


    def addmodel(self):
        a = str(input("输入你要添加的模型"))
        print()
        print("若要返回请按下[Q]")
        # 允许输入"q"退出
        if a.lower() == 'q':
            print("操作取消")
            return
        if "model_list" not in self.config:
            self.config["model_list"] = []  # 若键不存在，创建空列表
        elif not isinstance(self.config["model_list"], list):
            self.config["model_list"] = [self.config["model_list"]]  # 将现有值转换为列表
        if a not in self.config["model_list"]:
            self.config["model_list"].append(a)
        else:
            print(f"模型 '{a}' 已存在，未添加重复项")
            return
        SaveConfigData(self.config)
        print("完成添加！即将返回配置菜单...")
        time.sleep(1)
        return

    def delmodel(self):
        print("\n当前模型列表:")
        for i, group in enumerate(self.config.get("model_list", []), 1):
            print(f"{i}. {group}")
            print()
            print("若要返回请按下[Q]")
        if not self.config["model_list"]:
            print("没有可删除的模型")
            return
        try:
            index = int(input("输入要删除的模型编号: ")) - 1
            if 0 <= index < len(self.config["model_list"]):
                removed = self.config["model_list"].pop(index)
                SaveConfigData(self.config)
                print(f"已删除模型: {removed}")
            else:
                print("无效的编号\n")
                return
        except ValueError:
            print("无效指令！\n")
            return


    def addsys(self):
        # 获取用户输入
        title = input("输入模型称呼（必须为唯一）：").strip()
        sys = input("输入模型人设：").strip()
        print()
        print("若要返回请按下[Q]")

        # 允许输入"q"退出
        if title.lower() == 'q' or sys.lower() == "q":
            print("操作取消")
            return

        # 初始化字典结构
        if "SYSTEM_PROMPT" not in self.config:  # 建议更改键名以反映数据结构变化
            self.config["SYSTEM_PROMPT"] = {}
        elif not isinstance(self.config["SYSTEM_PROMPT"], dict):
            # 处理类型不匹配的情况（如旧数据是列表）
            self.config["SYSTEM_PROMPT"] = {}

        # 检查并添加数据
        if title in self.config["SYSTEM_PROMPT"]:
            print(f"角色称呼 '{title}' 已存在！")
            # 可选：询问是否覆盖
            if input("是否覆盖现有人设？(y/n): ").lower() == 'y':
                self.config["SYSTEM_PROMPT"][title] = sys
                print("人设已更新！")
            else:
                print("未作修改")
                return
        else:
            self.config["SYSTEM_PROMPT"][title] = sys
            print(f"称呼 '{title}' 添加成功！")

        # 保存配置
        SaveConfigData(self.config)
        return

    def delsys(self):
        print("\n当前角色列表:")
        persona_dict = self.config.get("SYSTEM_PROMPT", {})
        if not persona_dict:
            print("没有可删除的角色")
            return

        # 显示所有角色称呼（带序号）
        sorted_titles = sorted(persona_dict.keys())  # 按键名字母排序
        for i, title in enumerate(sorted_titles, 1):
            print(f"{i}. {title}")
            print()
            print("若要返回请按下[Q]")

        try:
            choice = input("输入要删除的角色编号: ")
            # 允许输入"q"退出
            if choice.lower() == 'q':
                print("操作取消")
                return

            index = int(choice) - 1
            if 0 <= index < len(sorted_titles):
                title_to_remove = sorted_titles[index]
                removed_persona = persona_dict.pop(title_to_remove)
                SaveConfigData(self.config)
                print(f"已删除角色: {title_to_remove} ({removed_persona[:30]}...)")
                print("删除成功！")
            else:
                print("无效的编号\n")
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
            print("3. 返回上一级菜单")
            try:
                choice = int(input("请选择操作: "))
                if choice == 1:
                    self.addgroup()
                if choice == 2:
                    self.delgroup()
                if choice == 3:
                    return
                else:
                    print("无效的编号\n")
                    return
            except ValueError:
                print("无效指令！\n")
                return

    def changemodelconfig(self):
        self.clear_console()

        groups = self.config.get("model_list", [])
        print("\n当前模型列表:")
        for i, group in enumerate(groups, 1):
            print(f"{i}. {group}")

        while True:
            self.clear_console()
            print("\n操作选项:")
            print("1. 指定模型")
            print("2. 添加模型")
            print("3. 删除群组")
            print("4. 返回上一级菜单")
            try:
                choice = int(input("请选择操作: "))
                if choice == 1:
                    self.chosemodel()
                if choice == 2:
                    self.addmodel()
                if choice == 3:
                    self.delmodel()
                if choice == 4:
                    return
                else:
                    print("无效的编号\n")
                    return
            except ValueError:
                print("无效指令！\n")
                return


    def changesystemconfig(self):
        self.clear_console()

        groups = self.config.get("SYSTEM_PROMPT", {})
        print("\n当前模型列表:")
        if not groups:
            print("(空)")
        else:
            for i, (nickname, persona) in enumerate(groups.items(), 1):
                print(f"{i}. {nickname}")
        while True:
            self.clear_console()
            print("\n操作选项:")
            print("1. 添加人设")
            print("2. 删除人设")
            print("3. 返回上一级菜单")
            try:
                choice = int(input("请选择操作: "))
                if choice == 1:
                    self.addsys()
                if choice == 2:
                    self.delsys()
                if choice == 3:
                    return
                else:
                    print("无效的编号\n")
                    return
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
                if cmd == 2:
                    self.changemodelconfig()
                if cmd == 3:
                    self.changesystemconfig()
                if cmd == 4:
                    return
                else:
                    print("无效的编号\n")
                    continue
            except ValueError:
                print("无效指令！\n")
                continue

    def mainmenu(self):
        while True:
            self.clear_console()
            # 显示菜单
            self._display_menu()
            try:
                cmd = int(input("输入数字并按下回车进行相应命令： "))
                if cmd == 1:
                    try:
                        if self.has_empty_value(self.config):
                            print("配置文件不完整！")
                            continue
                        else:
                            self.clear_console()
                            break
                    except json.JSONDecodeError:
                        print("JSON 格式错误")
                if cmd == 2:
                    self.configmenu()
                if cmd == 3:
                    sys.exit(0)
                else:
                    print("无效的编号\n")
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
        print("4.返回上一级菜单")
        print("=" * 20)



