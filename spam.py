import pyautogui 
import keyboard 
print(" göktuğğğğğğğğ spawns")
print("[1]while")
print("[2]for")
a=input("1,2 >>> ")
spwan=input(">>> ")
if a=="1":
    while 1:
        print("[+]spawn")
        pyautogui.write(spwan)
        pyautogui.press("enter")
elif a=="2":
    n=int(input("n "))
    for i in range (n):
        print("[+]spawn")
        pyautogui.write(spwan)
        pyautogui.press("enter")
    print("shut")
else:
    print("not fuc*")
    exit()