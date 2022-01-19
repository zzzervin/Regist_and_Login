from module1 import *

LNeme=[]
NPass=[]
quest=["L","S","E"]

while 1:
    ST=quest.index(input("(L)og_in, (S)ing_up, (E)xit >>>").upper())
    if ST==0:#Log_in
        LNeme=Failis('Logins.txt',LNeme)
        NPass=Failis('Pass.txt',NPass)
        Log(LNeme,NPass)
        print(LNeme)
    elif ST==1:#Sing_up
        LNeme=Failis('Logins.txt',LNeme)
        NPass=Failis('Pass.txt',NPass)
        Sing(LNeme,NPass)
        rida_salvistamine('Logins.txt')        
        print(LNeme)
    elif ST==2:#Exit
        print("Good bey")
        break
