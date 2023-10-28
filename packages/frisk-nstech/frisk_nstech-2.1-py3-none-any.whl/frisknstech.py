from time import *
from colorama import init, Fore, Style
def superprint(text, typetime=0,end_wrap=True,show_tip=False,color="white"):
    def sprintcolorerror():
        print(Fore.RED+'''/!\\ 错误！
颜色参数未应用：输入不合规！''')
    if color == "white":
        colorset=Fore.WHITE
    elif color == "red":
        colorset=Fore.RED
    elif color == "yellow":
        colorset=Fore.YELLOW
    elif color == "green":
        colorset=Fore.GREEN
    elif color == "cyan":
        colorset=Fore.CYAN
    elif color == "blue":
        colorset=Fore.BLUE
    elif color == "purple":
        colorset=Fore.MAGENTA
    elif color == "black":
        colorset=Fore.BLACK
    elif color == "BLACK":
        colorset=Fore.LIGHTBLACK_EX
    elif color == "RED":
        colorset=Fore.LIGHTRED_EX
    elif color == "YELLOW":
        colorset=Fore.LIGHTYELLOW_EX
    elif color == "GREEN":
        colorset=Fore.LIGHTGREEN_EX
    elif color == "CYAN":
        colorset=Fore.LIGHTCYAN_EX
    elif color == "BLUE":
        colorset=Fore.LIGHTBLUE_EX
    elif color == "PURPLE":
        colorset=Fore.LIGHTMAGENTA_EX
    else:
        colorset=Fore.WHITE
        sprintcolorerror()
    global index
    for index in text:
        print(colorset + index + Fore.RESET, end='', flush=True)
        sleep(typetime)
    if end_wrap==True:
        print()
    if show_tip==True:
        print()
        str(index)
        print("打印完成！库版本：23W41A 打印速度："+index)