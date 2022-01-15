from module1 import *

LNeme=["zzz"]
NPass=["123"]
quest=["L","S","E"]

while 1:
    ST=quest.index(input("(L)og_in, (S)ing_up, (E)xit >>>").upper())
    if ST==0:#Log_in
        Log(LNeme,NPass)
    elif ST==1:#Sing_up
        Sing(LNeme,NPass)        
        print(LNeme)
    elif ST==2:#Exit
        print("Good bey")
        break
