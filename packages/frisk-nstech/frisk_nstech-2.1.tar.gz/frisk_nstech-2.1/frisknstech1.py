from time import *
def superprint(text, typetime=0,end_wrap=True,show_tip=False):
    global index
    for index in text:
        print(index, end='', flush=True)
        sleep(typetime)
    if end_wrap==True:
        print()
    if show_tip==True:
        print()
        str(index)
        print("打印完成！库版本：23W41A 打印速度："+index)