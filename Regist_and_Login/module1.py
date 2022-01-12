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
    try:
        Login=NL.index(input("Log_in >>>"))
        Pass=NP.index(input("Pass >>>"))
        if Login==Pass:
            print("Hello")
    except ValueError:
        print("oops")

def Sing(A:list,):    
    NLogin=input("New_log_in >>>")
    if NLogin==A:
        print("ei ole")
    elif NLogin!=A:
        print("Hello",NLogin)        
        Npass=input("New_pass >>>")
        print("You new ",Npass)
        A.append(NLogin)
    


        
            
            
