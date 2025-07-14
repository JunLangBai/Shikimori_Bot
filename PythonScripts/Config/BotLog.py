from BotConfig import LogLevel

def CMD_Log(str):
    if LogLevel == LogLevel.info:
        return
    elif LogLevel == LogLevel.error:
        print(str)