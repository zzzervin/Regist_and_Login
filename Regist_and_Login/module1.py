def RPass():
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()  
    str4 = str0+str1+str2+str3   
    ls = list(str4)    
    random.shuffle(ls)   
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    return psword 

def Log(NL:list,NP:list):
    while 1:
        Login=NL.index(input("Log_in >>>"))
        Pass=NP.index(input("Pass >>>"))
        if Login==Pass:
            print("Hello")
            break
        else:        
            print("Password and login is wrong")

def Sing(A:list,B:list):    
    PC=False
    while 1:
        if PC==True:
                break
        NLogin=input("New_log_in >>>")
        if NLogin not in A:
            A.append(NLogin)
            Q=input("automaatne pass(1) or your pass(2)")
            if Q=="2":
                while 1:
                    Npass=input("New_pass >>>")
                    PC=Pcheck(Npass)
                    if PC==True:
                        print("You new pass",Npass)                
                        B.append(Npass)
                        break
                    else:
                         print("Your password does not match")
            elif Q=="1":
                RP=RPass()
                print("You new pass",RP)
                B.append(RP)
                break
            
        else:
            print("Name is already taken")
def Pcheck(pas:str)-> bool:
    spisok=list(pas)
    a=False
    pT=0
    for q in spisok:
        if q.isdigit(): 
            a=True
            pT+=1
        if q.isalpha():
            a=True
            pT+=1
        if q.isupper():
            a=True
            pT+=1
        if q.islower():
            a=True
            pT+=1
        if q in list("@.,:;!_*-+()/#¤%&£$€"):
            a=True
            pT+=1
        if pT>=8:
            check=True
        else:
            check=False
    return check   


        
            
            
