#現在値を取得
import pyautogui as pag
from time import sleep

print("中断するときはcrt+cを押してください")

try:
    while True:
        x,y=pag.position()
        position_str="X:"+str(x).rjust(10)+" Y:"+str(y).rjust(10)
        print(position_str,end="")
        print("\b"*len(position_str),end="",flush=True)
        sleep(0.1)
        
except KeyboardInterrupt:
    print("\n強制終了いたしました")
